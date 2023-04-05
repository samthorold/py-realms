import logging
from random import shuffle
from typing import Sequence

from cards.deck import PLAYER_STARTING_DECK
from models.action import Action
from models.card import Card
from models.deck import Deck
from models.enums import ActionType, CardType, Faction, Rule
from models.exceptions import UnknownAction
from models.player import Player, PlayerInterface


logger = logging.getLogger(__name__)


def player_setup(
    name: str, draw: int = 0, starting_deck: Sequence[Card] | None = None
) -> Player:
    starting_deck = (
        PLAYER_STARTING_DECK if starting_deck is None else starting_deck
    )
    deck = list(starting_deck)
    logger.debug("%s setup deck %s", name, deck)
    shuffle(deck)
    # players know what is in the opponent's deck at all times (at least online).
    # so don't draw the cards until the start of a player's turn.
    if draw:
        hand, deck = deck[:draw], deck[draw:]
    else:
        hand, deck = None, deck
    logger.debug("%s setup deck %s %s", name, hand, deck)
    return Player(name=name, deck=deck, hand=hand)


def deck_setup() -> Deck:
    deck = Deck()
    for _ in range(5):
        deck.draw()
    return deck


class Game:
    """Orchestrate the Deck and Players."""

    def __init__(
        self,
        deck: Deck | None = None,
        players: tuple[PlayerInterface, PlayerInterface] | None = None,
        hand_size: int = 5,
        first_hand_size: int = 3,
        current_player: int = 0,
    ) -> None:
        self.trade_deck = deck_setup() if deck is None else deck
        self._players = (
            tuple(
                [
                    player_setup(name="P1", draw=3),
                    player_setup(name="P2", draw=0),
                ]
            )
            if players is None
            else players
        )
        self._actions = [Action(type=ActionType.START_GAME)]
        self._hand_size = hand_size
        self._first_hand_size = first_hand_size
        self._current_player = current_player

    def get_current_player(self) -> PlayerInterface:
        return self._players[self._current_player]

    def hydrate_action(self, action: Action | ActionType | str) -> Action:
        if isinstance(action, str):
            action = ActionType.from_str(action)
            logger.debug("%r", action)
        if isinstance(action, ActionType):
            action = Action(type=action)
            logger.debug("%r", action)
        return action

    def add_action(self, action: Action) -> None:
        logger.debug("Add action %r", action)
        self._actions.append(action)

    def remove_action(self, action: Action) -> None:
        logger.debug("Remove action %r", action)
        self._actions.remove(action)

    def add_card_actions(self, card: Card) -> None:
        for action in card.actions:
            logger.debug("Game add action %r", action)
            self.add_action(action)

    def replace_action_with_always(self, action: Action) -> None:
        self.add_action(action.as_always())
        self.remove_action(action)

    def replace_ally_actions(self, pl: PlayerInterface, faction: Faction) -> None:
        actions = [
            action
            for action in self._actions
            if action.rule == Rule.ALLY and action.faction == faction
        ]
        for action in actions:
            if pl.ally_in_play(faction):
                self.replace_action_with_always(action)

    def replace_scrap_actions(self, pl: PlayerInterface, card: Card) -> None:
        actions = [
            action
            for action in self._actions
            if action.rule == Rule.SCRAP and action in card.actions
        ]
        for action in actions:
            self.replace_action_with_always(action)

    def action(self, action: Action | ActionType | str, idx: int = 0) -> None:
        """Perform one action.

        Actions may lead to more actions being placed in the backlog.

        Args:
            action: Action to perform.
            idx: Position in the player deck, trade row, etc.

        Returns:
            None

        Raises:
            UnknownActionType: The action type is not specified in the
                [ActionType][models.enums.ActionType] enum.
            UnknownAction: The action is not in the match statement
                within this function.

        """
        pl = self.get_current_player()
        logger.info("%s start action", pl)
        # raises UnknownActionType
        action = self.hydrate_action(action)
        logger.debug("idx=%s action=%r", idx, action)
        match action:
            case Action(type=ActionType.START_GAME, n=_, rule=_, faction=_):
                for _ in range(self._hand_size):
                    self.add_action(Action(type=ActionType.PLAY))

            case Action(type=ActionType.START_TURN, n=_, rule=_, faction=_):
                pl.new_hand()
                for _ in range(self._first_hand_size):
                    self.add_action(Action(type=ActionType.PLAY))

            case Action(type=ActionType.PLAY, n=_, rule=_, faction=_):
                card = pl.play(idx)
                self.add_card_actions(card)
                self.replace_ally_actions(pl, card.faction)

            case Action(
                type=ActionType.ACQUIRE, n=_, rule=Rule.ALWAYS, faction=_
            ):
                card = self.trade_deck.acquire(idx)
                top_of_deck = (
                    any(
                        a.type == ActionType.NEXT_SHIP_TOP_OF_DECK
                        and a.rule == Rule.ALWAYS
                        for a in self._actions
                    )
                    and card.type == CardType.SHIP
                )
                pl.acquire(card, top_of_deck)

            case Action(type=ActionType.SCRAP_IN_PLAY, n=_, rule=_):
                # not really a rule for doing this
                # but the card needs to have an action with a SCRAP rule.
                card = pl.in_play[idx]
                self.replace_scrap_actions(pl, card)

            case Action(type=ActionType.DRAW, n=n, rule=Rule.ALWAYS, faction=_):
                for _ in range(n):
                    pl.draw()

            case Action(
                type=ActionType.COMBAT, n=n, rule=Rule.ALWAYS, faction=_
            ):
                pl.add_combat(n)

            case Action(
                type=ActionType.TRADE, n=n, rule=Rule.ALWAYS, faction=_
            ):
                pl.add_trade(n)

            case _:
                raise UnknownAction(f"Not a known action {repr(action)}")

        self.remove_action(action)

        logger.info("%s end action", pl)

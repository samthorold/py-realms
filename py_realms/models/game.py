import logging
from random import shuffle
from typing import Sequence

from pydantic import BaseModel, Field

from py_realms.cards.deck import PLAYER_STARTING_DECK
from py_realms.models.action import Action
from py_realms.models.card import Card
from py_realms.models.deck import Deck
from py_realms.models.enums import ActionType, CardType, Faction, Rule
from py_realms.models.exceptions import UnknownAction, ActionUnavailable
from py_realms.models.player import Player


logger = logging.getLogger(__name__)


NUM_CARDS_START_GAME = 3
NUM_CARDS_START_TURN = 5


def player_setup(
    name: str, draw: int = 0, starting_deck: Sequence[Card] | None = None
) -> Player:
    """Default player starting state.

    Players know what is in the opponent's deck at all times but not their hand.
    At least this is the case in the online version of the game.
    So by default, don't draw any cards to the hand when setting up a player.

    Args:
        name: Player's display name.
        draw: How many cards to draw.
        starting_deck: Optional deck to setup player with.
            Defaults to the standard starting deck of scouts and vipers.

    Returns:
        Player
    """
    starting_deck = PLAYER_STARTING_DECK if starting_deck is None else starting_deck
    deck = list(starting_deck)
    logger.debug("%s setup deck %s", name, deck)
    shuffle(deck)
    if draw:
        hand, deck = deck[:draw], deck[draw:]
    else:
        hand, deck = [], deck
    logger.debug("%s setup deck %s %s", name, hand, deck)
    return Player(name=name, deck=deck, hand=hand)


def deck_setup() -> Deck:
    """Default deck starting state. Draws five cards to the trade deck.

    Returns:
        Deck
    """
    deck = Deck()
    for _ in range(5):
        deck.draw()
    return deck


def players_setup() -> tuple[Player, Player]:
    return (player_setup(name="P1", draw=3), player_setup(name="P2", draw=0))


class Game(BaseModel):
    """Orchestrate the Deck and Players."""

    deck: Deck = Field(default_factory=deck_setup)
    players: tuple[Player, Player] = Field(default_factory=players_setup)
    current_player: int = 0
    actions: list[Action] = [Action(type=ActionType.START_GAME, n=3)]

    def get_current_player(self) -> Player:
        return self.players[self.current_player]

    def hydrate_action(self, action: Action | ActionType | str) -> Action:
        if isinstance(action, str):
            # raises UnknownActionType
            action = ActionType.from_str(action)
            logger.debug("%r", action)
        if isinstance(action, ActionType):
            action = Action(type=action)
            logger.debug("%r", action)
        return action

    def add_action(self, action: Action) -> None:
        logger.debug("Add action %r", action)
        self.actions.append(action)

    def remove_action(self, action: Action) -> None:
        logger.debug("Remove action %r", action)
        self.actions.remove(action)

    def add_card_actions(self, card: Card) -> None:
        for action in card.actions:
            logger.debug("Game add action %r", action)
            self.add_action(action)

    def replace_action_with_always(self, action: Action) -> None:
        self.add_action(action.as_always())
        self.remove_action(action)

    def replace_ally_actions(self, pl: Player, faction: Faction) -> None:
        actions = [
            action
            for action in self.actions
            if action.rule == Rule.ALLY and action.faction == faction
        ]
        for action in actions:
            if pl.ally_in_play(faction):
                self.replace_action_with_always(action)

    def replace_scrap_actions(self, pl: Player, card: Card) -> None:
        actions = [
            action
            for action in self.actions
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
            ActionUnavailable: The action cannot be performed.
            UnknownActionType: The action type is not specified in the
                [ActionType][py_realms.models.enums.ActionType] enum.
            UnknownAction: The action is not in the match statement
                within this function.

        """
        pl = self.get_current_player()
        logger.info("%s start action", pl)
        # raises UnknownActionType
        action = self.hydrate_action(action)
        if action not in self.actions:
            logger.info("%r not available", action)
            raise ActionUnavailable(f"{action} not available")
        logger.debug("idx=%s action=%r", idx, action)
        match action:
            case Action(type=ActionType.START_GAME, n=n, rule=_, faction=_):
                for _ in range(n):
                    self.add_action(Action(type=ActionType.PLAY))

            case Action(type=ActionType.START_TURN, n=n, rule=_, faction=_):
                pl.new_hand()
                for _ in range(n):
                    self.add_action(Action(type=ActionType.PLAY))

            case Action(type=ActionType.PLAY, n=_, rule=_, faction=_):
                card = pl.play(idx)
                self.add_card_actions(card)
                self.replace_ally_actions(pl, card.faction)

            case Action(type=ActionType.ACQUIRE, n=_, rule=Rule.ALWAYS, faction=_):
                card = self.deck.acquire(idx)
                top_of_deck = (
                    any(
                        a.type == ActionType.NEXT_SHIP_TOP_OF_DECK
                        and a.rule == Rule.ALWAYS
                        for a in self.actions
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

            case Action(type=ActionType.COMBAT, n=n, rule=Rule.ALWAYS, faction=_):
                pl.add_combat(n)

            case Action(type=ActionType.TRADE, n=n, rule=Rule.ALWAYS, faction=_):
                pl.add_trade(n)

            case _:
                raise UnknownAction(f"Not a known action {repr(action)}")

        self.remove_action(action)

        logger.info("%s end action", pl)

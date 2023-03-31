import logging
from random import shuffle
from typing import Sequence

from cards.deck import PLAYER_STARTING_DECK
from models.action import Action
from models.card import Card
from models.deck import Deck
from models.enums import ActionType, Rule
from models.player import Player


logger = logging.getLogger(__name__)


def player_setup(
    name: str, draw: int = 0, starting_deck: Sequence[Card] | None = None
) -> Player:
    starting_deck = PLAYER_STARTING_DECK if starting_deck is None else starting_deck
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
        players: tuple[Player, Player] | None = None,
        hand_size: int = 5,
        first_hand_size: int = 3,
    ) -> None:
        self.trade_deck = deck_setup() if deck is None else deck
        self.players = (
            tuple(
                [
                    player_setup(name="P1", draw=3),
                    player_setup(name="P2", draw=0),
                ]
            )
            if players is None
            else players
        )
        self.actions: list[Action]
        self.hand_size = hand_size
        self.first_hand_size = first_hand_size

    def add_card_actions(self, card: Card) -> None:
        for action in card.actions:
            logger.debug("Game add action %r", action)
            self.actions.append(action)

    def action(
        self, pidx: int, action: Action, idx: int = 0, card: Card | None = None
    ) -> None:
        """Performs the action, if allowed."""
        # TODO: Actions and "using up" actions
        # Some kind of action queue / stack
        # Separate from the Card.actions (which is immutable anyway)
        # The actions dealt with here can push more actions onto the queue
        # with I guess ActionType.PLAY being the big one.
        # Don't know who owns the actions queue
        # ---
        # Removing "used" actions ...
        # Just a .remove on the actions list?
        # Not bothered which one really ...
        # just that there is one less of them.
        # Apart from a UI perspective
        # But there's a lot of work to do before any UI
        pl = self.players[pidx]
        logger.debug(f"%r", action)
        match action:
            case Action(type=ActionType.START_GAME, n=_, rule=_):
                for _ in range(self.hand_size):
                    self.actions.append(Action(type=ActionType.PLAY))
                    self.actions.remove(action)

            case Action(type=ActionType.START_TURN, n=_, rule=_):
                pl.new_hand()
                for _ in range(self.first_hand_size):
                    self.actions.append(Action(type=ActionType.PLAY))
                    self.actions.remove(action)

            case Action(type=ActionType.PLAY, n=n):
                card = pl.play(idx)
                self.add_card_actions(card)
                # Some kind of check on action rules being fulfilled
                # could replace rules fulfilled with ALWAYS actions
                self.actions.remove(action)

            case Action(type=ActionType.DRAW, n=n, rule=Rule.ALWAYS):
                pl.draw()
                self.actions.remove(action)

            case Action(type=ActionType.COMBAT, n=n, rule=Rule.ALWAYS):
                pl.combat += n
                self.actions.remove(action)

            case Action(type=ActionType.TRADE, n=n, rule=Rule.ALWAYS):
                pl.trade += n
                self.actions.remove(action)

            case Action(type=ActionType.COMBAT, n=n, rule=Rule.ALLY_IN_PLAY):
                if card is None:
                    raise ValueError(
                        f"Must provide a card for this action {repr(action)}"
                    )
                if pl.ally_in_play(card):
                    pl.combat += n
                    self.actions.remove(action)
            case _:
                raise ValueError(f"Not a known action {repr(action)}")

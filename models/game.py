import logging
from random import shuffle
from typing import Sequence

from cards.deck import PLAYER_STARTING_DECK
from models.card import Card
from models.deck import Deck
from models.player import Player


logger = logging.getLogger(__name__)


def player_setup(
    name: str, draw: int = 3, starting_deck: Sequence[Card] | None = None
) -> Player:
    starting_deck = PLAYER_STARTING_DECK if starting_deck is None else starting_deck
    deck = list(starting_deck)
    logger.debug("%s setup deck %s", name, deck)
    shuffle(deck)
    hand, deck = deck[:draw], deck[draw:]
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
        self, deck: Deck | None = None, players: tuple[Player, Player] | None = None
    ) -> None:
        self.trade_deck = deck_setup() if deck is None else deck
        self.players = (
            tuple(
                [
                    player_setup(name="P1", draw=3),
                    player_setup(name="P2", draw=5),
                ]
            )
            if players is None
            else players
        )

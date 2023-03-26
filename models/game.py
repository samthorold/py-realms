import logging
from random import shuffle
from typing import Sequence

from cards.deck import PLAYER_STARTING_DECK
from models.card import Card
from models.deck import Deck
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
        self, deck: Deck | None = None, players: tuple[Player, Player] | None = None
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

    def turn(self, player1: bool) -> None:
        pl = self.players[0 if player1 else 1]
        print(pl)
        if not pl.hand:
            pl.new_hand()
            print(pl)

    def play(self) -> None:
        player1 = True
        while True:
            self.turn(player1)
            break

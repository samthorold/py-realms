import logging
from random import shuffle

from cards.deck import GAME_STARTING_DECK
from cards.factionless import EXPLORER
from models.card import Card

logger = logging.getLogger(__name__)


class Deck:
    def __init__(self, shuffle_on_init: bool = True):
        self.explorers = [EXPLORER] * 20
        self.remaining = list(GAME_STARTING_DECK)
        self.in_play: list[Card]
        if shuffle_on_init:
            shuffle(self.remaining)

    def select_card(self, idx: int) -> Card:
        logger.debug("Deck select card %s", idx)
        card = self.in_play.pop(idx)
        logger.debug("Deck select card %r", card)
        return card

    def draw(self) -> None:
        card = self.remaining.pop()
        logger.debug("Deck draw %r", card)
        self.in_play.append(card)

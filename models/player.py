import logging
from random import shuffle
from cards.deck import PLAYER_STARTING_DECK

from models.card import Card


logger = logging.getLogger(__name__)


class Player:
    def __init__(self, name: str):
        self.name = name
        self.deck = list(PLAYER_STARTING_DECK)
        self.hand: list[Card] = []
        self.discard_pile: list[Card] = []
        self.in_play: list[Card] = []

    def discard_from_hand(self, idx: int) -> None:
        logger.debug("%s discarding from hand %s", self.name, idx)
        card = self.hand.pop(idx)
        logger.debug("%s discarding from hand %r", self.name, card)
        self.discard_pile.append(card)
        logger.debug("%s discard pile length %s", self.name, len(self.discard_pile))

    def scrap_from_hand(self, idx: int) -> None:
        logger.debug("%s scrapping from hand %s", self.name, idx)
        card = self.hand.pop(idx)
        logger.debug("%s scrapping from hand %r", self.name, card)

    def scrap_from_discard_pile(self, idx: int) -> None:
        logger.debug("%s scrapping from discard pile %s", self.name, idx)
        card = self.discard_pile.pop(idx)
        logger.debug("%s scrapping from discard pile %r", self.name, card)

    def draw(self) -> Card:
        if not self.deck:
            self.deck = list(self.discard_pile)
            shuffle(self.deck)
            self.discard_pile = []
        return self.deck.pop()

    def new_hand(self) -> None:
        while len(self.hand) < 5:
            self.hand.append(self.draw())

import logging
from random import shuffle

from cards.deck import GAME_STARTING_DECK
from cards.factionless import EXPLORER
from models.card import Card

logger = logging.getLogger(__name__)


class Deck:
    def __init__(self, shuffle_on_init: bool = True):
        self.explorers = [EXPLORER] * 20
        self.trade_deck = list(GAME_STARTING_DECK)
        self.trade_row: list[Card] = []
        if shuffle_on_init:
            shuffle(self.trade_deck)

    def acquire(self, idx: int) -> Card:
        """Returns the Card in the trade row at `idx` and draws another card."""
        logger.debug("Deck select card %s", idx)
        card = self.trade_row.pop(idx)
        logger.debug("Deck select card %r", card)
        self.draw()
        return card

    def scrap(self, idx: int) -> None:
        """Scraps the Card in the trade row at `idx` and draws another card."""
        logger.debug("Deck select card %s", idx)
        card = self.trade_row.pop(idx)
        logger.debug("Deck select card %r", card)
        self.draw()
        return

    def acquire_explorer(self) -> Card:
        """Returns an Explorer."""
        logger.debug("Deck select explorer")
        card = self.explorers.pop()
        logger.debug("Deck select card %r", card)
        # self.draw()  # noop these days anyway
        return card

    def draw(self) -> None:
        """Draw another card from the trade deck.

        No op if

        - trade deck empty.
        - trade row already has 5 cards.

        """
        if self.trade_deck:
            if len(self.trade_row) < 5:
                card = self.trade_deck.pop()
                logger.debug("Deck draw %r", card)
                self.trade_row.append(card)
            else:
                logger.debug("Trade row has 5 cards")

        else:
            logger.debug("Deck trade deck empty")

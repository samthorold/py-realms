import logging
from random import shuffle

from pydantic import BaseModel, Field

from py_realms.cards.deck import GAME_STARTING_DECK
from py_realms.cards.factionless import EXPLORER
from py_realms.models.card import Card

logger = logging.getLogger(__name__)


NUM_CARDS_TRADE_DECK = 5


def get_shuffled_deck() -> list[Card]:
    deck = list(GAME_STARTING_DECK)
    shuffle(deck)
    return deck


class Deck(BaseModel):
    explorers: list[Card] = [EXPLORER] * 20
    trade_deck: list[Card] = Field(default_factory=get_shuffled_deck)
    trade_row: list[Card] = []

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
        return card

    def draw(self) -> None:
        """Draw another card from the trade deck.

        No op if

        - trade deck empty.
        - trade row already has 5 cards.

        """
        if self.trade_deck:
            if len(self.trade_row) < NUM_CARDS_TRADE_DECK:
                card = self.trade_deck.pop()
                logger.debug("Deck draw %r", card)
                self.trade_row.append(card)
            else:
                logger.debug("Trade row has 5 cards")

        else:
            logger.debug("Deck trade deck empty")

import pytest

from models.card import Card
from models.deck import Deck


@pytest.fixture
def deck() -> Deck:
    deck = Deck()
    for _ in range(5):
        deck.draw()
    return deck


def test_init(deck: Deck) -> None:
    assert deck.explorers
    assert deck.trade_row


def test_draw_never_goes_above_5_cards_in_trade_row() -> None:
    deck = Deck()
    for _ in range(25):
        deck.draw()
    assert len(deck.trade_row) == 5


def test_draw_with_no_trade_deck_noop() -> None:
    deck = Deck()
    deck.trade_deck = []
    deck.draw()


def test_acquire(deck: Deck) -> None:
    og_deck = len(deck.trade_deck)
    card = deck.acquire(0)
    assert isinstance(card, Card)
    assert card.name.lower() != "explorer"
    assert len(deck.trade_row) == 5
    assert len(deck.trade_deck) == og_deck - 1


def test_scrap(deck: Deck) -> None:
    og_deck = len(deck.trade_deck)
    deck.scrap(0)
    assert len(deck.trade_row) == 5
    assert len(deck.trade_deck) == og_deck - 1


def test_acquire_explorer(deck: Deck) -> None:
    og_deck = len(deck.trade_deck)
    card = deck.acquire_explorer()
    assert isinstance(card, Card)
    assert card.name.lower() == "explorer"
    assert len(deck.trade_row) == 5
    assert len(deck.trade_deck) == og_deck

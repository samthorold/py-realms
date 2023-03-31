import logging
from random import shuffle
from cards.deck import PLAYER_STARTING_DECK

from models.card import Card
from models.enums import CardType, Faction


logger = logging.getLogger(__name__)


class Player:
    """
    Examples:
    >>> player = Player(name="Player 1")
    >>> player.authority
    50


    """

    def __init__(
        self,
        name: str,
        authority: int = 50,
        trade: int = 0,
        combat: int = 0,
        deck: list[Card] | None = None,
        hand: list[Card] | None = None,
        discard_pile: list[Card] | None = None,
        in_play: list[Card] | None = None,
    ):
        self.name = name
        self.authority = authority
        self.trade = trade
        self.combat = combat
        self.deck = [] if deck is None else deck
        self.hand = [] if hand is None else hand
        self.discard_pile = [] if discard_pile is None else discard_pile
        self.in_play = [] if in_play is None else in_play

    def __repr__(self) -> str:
        return (
            f"<Player(name={self.name}, authority={self.authority}, "
            f"trade={self.trade}, combat={self.combat}, in_play={self.in_play}, "
            f"deck={self.deck}, hand={self.hand}, discard_pile={self.discard_pile})>"
        )

    @property
    def ships_in_play(self) -> tuple[Card, ...]:
        return tuple(c for c in self.in_play if c.type == CardType.SHIP)

    @property
    def bases_in_play(self) -> tuple[Card, ...]:
        return tuple(
            c for c in self.in_play if c.type in [CardType.OUTPOST, CardType.BASE]
        )

    @property
    def outposts_in_play(self) -> tuple[Card, ...]:
        return tuple(c for c in self.in_play if c.type == CardType.OUTPOST)

    def ally_in_play(self, faction: Faction) -> bool:
        return any(faction == c.faction for c in self.in_play)

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

    def scrap_from_trade_row(self, idx: int) -> int:
        logger.debug("%s scrapping from trade row %s", self.name, idx)
        return idx

    def draw(self) -> None:
        if not self.deck:
            logger.debug("%s shuffling discard pile and moving to deck", self.name)
            self.deck = list(self.discard_pile)
            shuffle(self.deck)
            self.discard_pile = []
        card = self.deck.pop()
        logger.debug("%s draw %s", self.name, card)
        self.hand.append(card)

    def play(self, idx: int) -> Card:
        if not self.hand:
            logger.debug("%s no cards to play (%s)", self.name, idx)
            raise ValueError("No cards to play")
        card = self.hand.pop()
        logger.debug("%s play %s", self.name, card)
        self.in_play.append(card)
        return card

    def acquire(self, card: Card, top_of_deck: bool = False) -> None:
        if top_of_deck:
            self.deck.append(card)
        else:
            self.discard_pile.append(card)

    def new_hand(self) -> None:
        logger.debug("%s new hand", self.name)
        if not self.hand:
            for _ in range(5):
                self.draw()

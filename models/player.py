import logging
from random import shuffle

from pydantic import BaseModel

from models.card import Card
from models.enums import CardType, Faction


logger = logging.getLogger(__name__)


class Player(BaseModel):
    """
    Examples:

        >>> player = Player(name="Player 1")
        >>> player.authority
        50


    """

    name: str
    authority: int = 50
    trade: int = 0
    combat: int = 0
    deck: list[Card] = []
    hand: list[Card] = []
    discard_pile: list[Card] = []
    in_play: list[Card] = []

    def __repr__(self) -> str:
        return (
            f"<Player(name={self.name}, authority={self.authority},"
            f" trade={self.trade}, combat={self.combat},"
            f" in_play={self.in_play}, deck={self.deck}, hand={self.hand},"
            f" discard_pile={self.discard_pile})>"
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

    def add_combat(self, combat: int) -> int:
        logger.debug("%s adding %s combat to %s", self.name, combat, self.combat)
        self.combat += combat
        logger.debug("%s combat %s", self.name, self.combat)
        return self.combat

    def add_authority(self, authority: int) -> int:
        logger.debug("%s adding %s authority to %s", self.name, authority, self.combat)
        self.authority += authority
        logger.debug("%s authority %s", self.name, self.authority)
        return self.authority

    def add_trade(self, trade: int) -> int:
        logger.debug("%s adding %s trade to %s", self.name, trade, self.trade)
        self.trade += trade
        logger.debug("%s trade %s", self.name, self.trade)
        return self.trade

    def ally_in_play(self, faction: Faction) -> bool:
        return any(c.faction in (faction, Faction.ALL) for c in self.in_play)

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
        card = self.hand.pop(idx)
        logger.debug("%s play %s", self.name, card)
        self.in_play.append(card)
        # adding trade and combat etc. are actions and handled by `Game`.
        return card

    def acquire(self, card: Card, top_of_deck: bool = False) -> None:
        logger.debug("%s acquire %r (top %s)", self.name, card, top_of_deck)
        if top_of_deck:
            self.deck.append(card)
        else:
            self.discard_pile.append(card)
        self.trade -= card.cost
        logger.debug("%s trade %s", self.name, self.trade)

    def new_hand(self) -> None:
        logger.debug("%s new hand", self.name)
        if not self.hand:
            for _ in range(5):
                self.draw()

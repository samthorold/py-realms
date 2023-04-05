import logging
from random import shuffle
from typing import Protocol

from models.card import Card
from models.enums import CardType, Faction


logger = logging.getLogger(__name__)


class PlayerInterface(Protocol):

    @property
    def in_play(self) -> tuple[Card, ...]:...
    @property
    def hand(self) -> tuple[Card, ...]:...
    @property
    def ships_in_play(self) -> tuple[Card, ...]:
        ...

    @property
    def bases_in_play(self) -> tuple[Card, ...]: ...

    @property
    def outposts_in_play(self) -> tuple[Card, ...]: ...

    def add_combat(self, combat: int) -> int: ...

    def get_authority(self) -> int: ...

    def add_authority(self, authority: int) -> int: ...

    def add_trade(self, trade: int) -> int: ...

    def ally_in_play(self, faction: Faction) -> bool: ...

    def discard_from_hand(self, idx: int) -> None: ...

    def scrap_from_hand(self, idx: int) -> None: ...

    def scrap_from_discard_pile(self, idx: int) -> None: ...

    def scrap_from_trade_row(self, idx: int) -> int: ...

    def draw(self) -> None:
        ...

    def play(self, idx: int) -> Card: ...

    def acquire(self, card: Card, top_of_deck: bool = False) -> None: ...

    def new_hand(self) -> None: ...


class Player:
    """
    Examples:

        >>> player = Player(name="Player 1")
        >>> player.get_authority()
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
        self._authority = authority
        self._trade = trade
        self._combat = combat
        self._deck = [] if deck is None else deck
        self._hand = [] if hand is None else hand
        self._discard_pile = [] if discard_pile is None else discard_pile
        self._in_play = [] if in_play is None else in_play

    def __repr__(self) -> str:
        return (
            f"<Player(name={self.name}, authority={self._authority},"
            f" trade={self._trade}, combat={self._combat},"
            f" in_play={self._in_play}, deck={self._deck}, hand={self._hand},"
            f" discard_pile={self._discard_pile})>"
        )

    @property
    def in_play(self) -> tuple[Card, ...]:
        return tuple(self._in_play)

    @property
    def hand(self) -> tuple[Card, ...]:
        return tuple(self._hand)

    @property
    def ships_in_play(self) -> tuple[Card, ...]:
        return tuple(c for c in self._in_play if c.type == CardType.SHIP)

    @property
    def bases_in_play(self) -> tuple[Card, ...]:
        return tuple(
            c
            for c in self._in_play
            if c.type in [CardType.OUTPOST, CardType.BASE]
        )

    @property
    def outposts_in_play(self) -> tuple[Card, ...]:
        return tuple(c for c in self._in_play if c.type == CardType.OUTPOST)

    def add_combat(self, combat: int) -> int:
        logger.debug(
            "%s adding %s combat to %s", self.name, combat, self._combat
        )
        self._combat += combat
        logger.debug("%s combat %s", self.name, self._combat)
        return self._combat

    def get_authority(self) -> int:
        return self._authority

    def add_authority(self, authority: int) -> int:
        logger.debug(
            "%s adding %s authority to %s", self.name, authority, self._combat
        )
        self._authority += authority
        logger.debug("%s authority %s", self.name, self._authority)
        return self._authority

    def add_trade(self, trade: int) -> int:
        logger.debug("%s adding %s trade to %s", self.name, trade, self._trade)
        self._trade += trade
        logger.debug("%s trade %s", self.name, self._trade)
        return self._trade

    def ally_in_play(self, faction: Faction) -> bool:
        return any(faction == c.faction for c in self._in_play)

    def discard_from_hand(self, idx: int) -> None:
        logger.debug("%s discarding from hand %s", self.name, idx)
        card = self._hand.pop(idx)
        logger.debug("%s discarding from hand %r", self.name, card)
        self._discard_pile.append(card)
        logger.debug(
            "%s discard pile length %s", self.name, len(self._discard_pile)
        )

    def scrap_from_hand(self, idx: int) -> None:
        logger.debug("%s scrapping from hand %s", self.name, idx)
        card = self._hand.pop(idx)
        logger.debug("%s scrapping from hand %r", self.name, card)

    def scrap_from_discard_pile(self, idx: int) -> None:
        logger.debug("%s scrapping from discard pile %s", self.name, idx)
        card = self._discard_pile.pop(idx)
        logger.debug("%s scrapping from discard pile %r", self.name, card)

    def scrap_from_trade_row(self, idx: int) -> int:
        logger.debug("%s scrapping from trade row %s", self.name, idx)
        return idx

    def draw(self) -> None:
        if not self._deck:
            logger.debug(
                "%s shuffling discard pile and moving to deck", self.name
            )
            self._deck = list(self._discard_pile)
            shuffle(self._deck)
            self._discard_pile = []
        card = self._deck.pop()
        logger.debug("%s draw %s", self.name, card)
        self._hand.append(card)

    def play(self, idx: int) -> Card:
        if not self._hand:
            logger.debug("%s no cards to play (%s)", self.name, idx)
            raise ValueError("No cards to play")
        card = self._hand.pop(idx)
        logger.debug("%s play %s", self.name, card)
        self._in_play.append(card)
        return card

    def acquire(self, card: Card, top_of_deck: bool = False) -> None:
        if top_of_deck:
            self._deck.append(card)
        else:
            self._discard_pile.append(card)

    def new_hand(self) -> None:
        logger.debug("%s new hand", self.name)
        if not self._hand:
            for _ in range(5):
                self.draw()

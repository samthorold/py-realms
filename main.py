from dataclasses import dataclass
from enum import Enum, auto
import logging
from random import shuffle


logger = logging.getLogger(__name__)


class Faction(Enum):
    IMPERIAL = auto()    # yellow
    MACHINE = auto()     # red
    FEDERATION = auto()  # blue
    BLOB = auto()        # green


class Rule(Enum):
    ALWAYS = auto()
    SAME_FACTION_IN_PLAY = auto()
    SCRAP = auto()


@dataclass
class Action:
    attack: int = 0
    health: int = 0
    rule: Rule = Rule.ALWAYS


@dataclass
class Card:
    name: str
    cost: int
    actions: list[Action]
    money: int = 0


VIPER = Card(name="viper", cost=0, actions=[Action(attack=1)])
SCOUT = Card(name="scout", cost=0, money=1, actions=[])


EXPLORER = Card(
    name="explorer",
    cost=2,
    money=2,
    actions=[Action(attack=2, rule=Rule.SCRAP)],
)


CUTTER = Card(
    name="cutter",
    cost=2,
    money=2,
    actions=[
        Action(health=4),
        Action(attack=4, rule=Rule.SAME_FACTION_IN_PLAY),
    ]
)


FEDERATION_SHUTTLE = Card(
    name="federation shuttle",
    cost=1,
    money=2,
    actions=[
        Action(health=4, rule=Rule.SAME_FACTION_IN_PLAY),
    ]
)


PLAYER_STARTING_DECK = tuple(
    [VIPER] * 2 + [SCOUT] * 5
)


GAME_STARTING_DECK = tuple(
    [CUTTER] * 4 +
    [FEDERATION_SHUTTLE] * 4
)


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


class Game:
    """Orchestrate the Deck and Players."""


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    print("Py Realms - a Python implementation of Star Realms")
    deck = Deck()
    player1 = Player(name="Player 1")
    player2 = Player(name="Player 2")

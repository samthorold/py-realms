from enum import Enum, auto


class Faction(Enum):
    NONE = auto()
    IMPERIAL = auto()  # yellow
    MACHINE = auto()  # red
    FEDERATION = auto()  # blue
    BLOB = auto()  # green


class Rule(Enum):
    ALWAYS = auto()
    ALLY_IN_PLAY = auto()
    SCRAP = auto()


class CardType(Enum):
    BASE = auto()
    SHIP = auto()
    OUTPOST = auto()


class ActionType(Enum):
    TRADE = auto()  # accrue trade combat saved up
    COMBAT = auto()  # accrue the combat saved up
    AUTHORITY = auto()  # use authority
    SCRAP_TRADE = auto()
    ACQUIRE_TOP = auto()
    DESTROY_BASE = auto()
    DRAW = auto()
    PLAY = auto()  # play a card from hand
    ACQUIRE = auto()  # acquire a card from the trade row
    ATTACK = auto()  # use the combat saved up
    START_GAME = auto()  # get 3 PLAY actions and perhaps more in the future
    START_TURN = auto()  # get 5 PLAY actions
    OPPONENT_DISCARD = auto()

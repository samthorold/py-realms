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


class Type(Enum):
    BASE = auto()
    SHIP = auto()
    OUTPOST = auto()


class ActionType(Enum):
    WEALTH = auto()
    ATTACK = auto()
    HEALTH = auto()
    SCRAP_TRADE = auto()
    ACQUIRE_TOP = auto()
    DESTROY_BASE = auto()
    DRAW = auto()

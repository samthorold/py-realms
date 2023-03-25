from enum import Enum, auto


class Faction(Enum):
    NONE = auto()
    IMPERIAL = auto()  # yellow
    MACHINE = auto()  # red
    FEDERATION = auto()  # blue
    BLOB = auto()  # green


class Rule(Enum):
    ALWAYS = auto()
    SAME_FACTION_IN_PLAY = auto()
    SCRAP = auto()


class Type(Enum):
    BASE = auto()
    SHIP = auto()
    OUTPOST = auto()

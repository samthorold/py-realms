from __future__ import annotations
from enum import Enum, auto

from models.exceptions import UnknownActionType


class Faction(Enum):
    """Card allegiances"""

    NONE = auto()
    IMPERIAL = auto()  # yellow
    MACHINE = auto()  # red
    FEDERATION = auto()  # blue
    BLOB = auto()  # green


class Rule(Enum):
    """When an [ActionType][models.enums.ActionType] can be played."""

    ALWAYS = auto()
    ALLY = auto()
    SCRAP = auto()


class CardType(Enum):
    BASE = auto()
    SHIP = auto()
    OUTPOST = auto()


class ActionType(Enum):
    """Types of actions executed during play."""

    TRADE = "TRADE"  # accrue trade combat saved up
    COMBAT = "COMBAT"  # accrue the combat saved up
    AUTHORITY = "AUTHORITY"  # use authority
    SCRAP_TRADE = "SCRAP_TRADE"
    ACQUIRE_TOP = "ACQUIRE_TOP"
    DESTROY_BASE = "DESTROY_BASE"
    DRAW = "DRAW"
    PLAY = "PLAY"  # play a card from hand
    ACQUIRE = "ACQUIRE"  # acquire a card from the trade row
    ATTACK = "ATTACK"  # use the combat saved up
    START_GAME = "START_GAME"  # get 3 PLAY actions and perhaps more in the future
    START_TURN = "START_TURN"  # get 5 PLAY actions
    OPPONENT_DISCARD = "OPPONENT_DISCARD"
    DISCARD = "DISCARD"
    NEXT_SHIP_TOP_OF_DECK = "NEXT_SHIP_TOP_OF_DECK"

    @classmethod
    def from_str(cls, string: str) -> ActionType:
        try:
            return cls(string.upper().strip())
        except ValueError:
            # No from e here
            # this is the start of the problem from a py-realms perspective
            raise UnknownActionType(string)

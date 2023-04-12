from __future__ import annotations
from enum import Enum

from models.exceptions import UnknownActionType


class Faction(Enum):
    """Card allegiances"""

    NONE = "."
    IMPERIAL = "IMPERIAL"  # yellow
    MACHINE = "MACHINE"  # red
    FEDERATION = "FEDERATION"  # blue
    BLOB = "BLOB"  # green
    ALL = "ALL"


class Rule(Enum):
    """When an [ActionType][models.enums.ActionType] can be played."""

    ALWAYS = "ALWAYS"
    ALLY = "ALLY"
    SCRAP = "SCRAP"
    BASES_IN_PLAY_2 = "BASES_IN_PLAY_2"


class CardType(Enum):
    BASE = "BASE"
    SHIP = "SHIP"
    OUTPOST = "OUTPOST"


class ActionType(Enum):
    """Types of actions executed during play."""

    TRADE = "TRADE"  # accrue trade combat saved up
    COMBAT = "COMBAT"  # accrue the combat saved up
    AUTHORITY = "AUTHORITY"  # use authority
    SCRAP_TRADE = "SCRAP_TRADE"
    SCRAP_HAND_OR_DISCARD = "SCRAP_HAND_OR_DISCARD"
    SCRAP_HAND_OR_DISCARD_THEN_DRAW = "SCRAP_HAND_OR_DISCARD_THEN_DRAW"
    SCRAP_IN_PLAY = "SCRAP_IN_PLAY"
    ACQUIRE_TOP = "ACQUIRE_TOP"
    DESTROY_BASE = "DESTROY_BASE"
    DRAW = "DRAW"
    DRAW_THEN_SCRAP_FROM_HAND = "DRAW_THEN_SCRAP_FROM_HAND"
    PLAY = "PLAY"  # play a card from hand
    ACQUIRE = "ACQUIRE"  # acquire a card from the trade row
    ATTACK = "ATTACK"  # use the combat saved up
    START_GAME = "START_GAME"  # get 3 PLAY actions
    START_TURN = "START_TURN"  # get 5 PLAY actions
    END_TURN = "END_TURN"
    OPPONENT_DISCARD = "OPPONENT_DISCARD"
    DISCARD = "DISCARD"
    NEXT_SHIP_TOP_OF_DECK = "NEXT_SHIP_TOP_OF_DECK"
    TRADE_3_OR_COMBAT_5 = "TRADE_3_OR_COMBAT_5"
    COPY_CARD = "COPY_CARD"
    COMBAT_5_OR_DRAW_FOR_EACH_BLOB = "COMBAT_5_OR_DRAW_FOR_EACH_BLOB"
    DRAW_AND_DESTROY_TARGET_BASE = "DRAW_AND_DESTROY_TARGET_BASE"
    COMBAT_ON_PLAY_SHIP = "COMBAT_ON_PLAY_SHIP"
    DISCARD_THEN_DRAW = "DISCARD_THEN_DRAW"
    TRADE_2_OR_AUTHORITY_2 = "TRADE_2_OR_AUTHORITY_2"
    COMBAT_2_OR_AUTHORITY_3 = "COMBAT_2_OR_AUTHORITY_3"

    @classmethod
    def from_str(cls, string: str) -> ActionType:
        try:
            return cls(string.upper().strip())
        except ValueError:
            # No from e here
            # this is the start of the problem from a py-realms perspective
            raise UnknownActionType(string)

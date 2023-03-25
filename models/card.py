from dataclasses import dataclass

from models.action import Action
from models.enums import Faction, Type


@dataclass
class Card:
    name: str
    type: Type
    faction: Faction
    cost: int
    actions: list[Action]
    money: int = 0

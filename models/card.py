from dataclasses import dataclass

from models.action import Action
from models.enums import Faction, Type


@dataclass
class Card:
    """
    Examples:
    >>> from models.enums import Faction, Type
    >>> Card(
    ...     name="scout",
    ...     type=Type.SHIP,
    ...     faction=Faction.NONE,
    ...     cost=0,
    ...     money=1,
    ...     actions=[],
    ... )
    Card(name='scout', type=<Type.SHIP: 2>, faction=<Faction.NONE: 1>, cost=0, actions=[], money=1)

    """

    name: str
    type: Type
    faction: Faction
    cost: int
    actions: list[Action]
    money: int = 0

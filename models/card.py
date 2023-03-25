from dataclasses import dataclass

from models.action import Action
from models.enums import Faction, Type


@dataclass
class Card:
    """
    Examples:
    >>> from models.action import Action
    >>> from models.enums import Faction, Rule, Type
    >>> Card(
    ...     name="scout",
    ...     type=Type.SHIP,
    ...     faction=Faction.NONE,
    ...     cost=0,
    ...     actions=[Action(wealth=1, rule=Rule.ALWAYS)],
    ... )
    Card(name='scout', type=<Type.SHIP: 2>, faction=<Faction.NONE: 1>, cost=0, actions=[Action(wealth=1, attack=0, health=0, rule=<Rule.ALWAYS: 1>)], defense=0)

    """

    name: str
    type: Type
    faction: Faction
    cost: int
    actions: list[Action]
    defense: int = 0

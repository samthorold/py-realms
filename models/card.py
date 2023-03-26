from dataclasses import dataclass

from models.action import Action
from models.enums import Faction, CardType


@dataclass(frozen=True)
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
    type: CardType
    faction: Faction
    cost: int
    actions: tuple[Action, ...]
    defense: int = 0

    def __repr__(self) -> str:
        return self.name

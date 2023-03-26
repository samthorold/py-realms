from dataclasses import dataclass

from models.action import Action
from models.enums import Faction, CardType


@dataclass(frozen=True)
class Card:
    """
    Examples:
    >>> from models.action import Action
    >>> from models.enums import ActionType, CardType, Faction, Rule
    >>> card = Card(
    ...     name="scout",
    ...     type=CardType.SHIP,
    ...     faction=Faction.NONE,
    ...     cost=0,
    ...     actions=[Action(n=1, type=ActionType.AUTHORITY, rule=Rule.ALWAYS)],
    ... )


    """

    name: str
    type: CardType
    faction: Faction
    cost: int
    actions: tuple[Action, ...]
    defense: int = 0

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        faction = self.faction
        actions = "\n".join(f"  {a}" for a in self.actions)
        return f"{self.name}: {faction} ({self.cost})\n{actions}"

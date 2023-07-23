from pydantic import BaseModel

from py_realms.models.action import Action
from py_realms.models.enums import Faction, CardType


class Card(BaseModel):
    """
    Examples:

        >>> from models.action import Action
        >>> from models.enums import ActionType, CardType, Faction, Rule
        >>> Card(
        ...     name="scout",
        ...     type=CardType.SHIP,
        ...     faction=Faction.NONE,
        ...     cost=0,
        ...     actions=[Action(n=1, type=ActionType.AUTHORITY, rule=Rule.ALWAYS)],
        ... )
        <Card(name=scout, type=CardType.SHIP, faction=Faction.NONE, cost=0, actions=(<Action(type=ActionType.AUTHORITY, n=1, rule=Rule.ALWAYS, faction=Faction.NONE)>,), defense=0)>


    """

    name: str
    type: CardType
    faction: Faction
    cost: int
    actions: tuple[Action, ...]
    defense: int = 0

    def __repr__(self) -> str:
        return (
            f"<Card(name={self.name}, type={self.type}, faction={self.faction},"
            f" cost={self.cost}, actions={self.actions},"
            f" defense={self.defense})>"
        )

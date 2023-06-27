from models.action import Action
from models.enums import Faction, CardType


class Card:
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

    def __init__(
        self,
        name: str,
        type: CardType,
        faction: Faction,
        cost: int,
        actions: tuple[Action, ...] = tuple(),
        defense: int = 0,
    ):
        self.name = name
        self.type = type
        self.faction = faction
        self.cost = cost
        self.actions = tuple(
            Action(type=a.type, n=a.n, rule=a.rule, faction=faction) for a in actions
        )
        self.defense = defense

    def __repr__(self) -> str:
        return (
            f"<Card(name={self.name}, type={self.type}, faction={self.faction},"
            f" cost={self.cost}, actions={self.actions},"
            f" defense={self.defense})>"
        )

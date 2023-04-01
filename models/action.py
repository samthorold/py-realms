from __future__ import annotations
from dataclasses import dataclass

from models.enums import ActionType, Faction, Rule


@dataclass(frozen=True)
class Action:
    """What, when, and how many times an action can be executed.

    - What: [models.enums.ActionType][]
    - When: [models.enums.Rule][] and [models.enums.Faction][]
    - How many: `n`

    """

    type: ActionType
    n: int = 1
    rule: Rule = Rule.ALWAYS
    faction: Faction = Faction.NONE

    def __repr__(self) -> str:
        return (
            f"<Action(type={self.type}, n={self.n}, rule={self.rule}, "
            f"faction={self.faction})>"
        )

    def as_always(self) -> Action:
        return Action(
            type=self.type,
            n=self.n,
            rule=Rule.ALWAYS,
            faction=self.faction,
        )

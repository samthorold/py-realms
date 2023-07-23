from __future__ import annotations

from pydantic import BaseModel

from py_realms.models.enums import ActionType, Faction, Rule


class Action(BaseModel):
    """What, when, and how many times an action can be executed.

    - What: [py_realms.models.enums.ActionType][]
    - When: [py_realms.models.enums.Rule][] and [py_realms.models.enums.Faction][]
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

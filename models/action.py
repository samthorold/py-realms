from dataclasses import dataclass

from models.enums import ActionType, Rule


@dataclass(frozen=True)
class Action:
    type: ActionType
    n: int
    rule: Rule = Rule.ALWAYS

    def __str__(self) -> str:
        rule = f" {self.rule}" if self.rule != Rule.ALWAYS else ""
        return f"({self.n}) {self.type}{rule}"

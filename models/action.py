from dataclasses import dataclass

from models.enums import ActionType, Rule


@dataclass
class Action:
    type: ActionType
    n: int
    rule: Rule = Rule.ALWAYS

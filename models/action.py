from dataclasses import dataclass

from models.enums import Rule


@dataclass
class Action:
    attack: int = 0
    health: int = 0
    rule: Rule = Rule.ALWAYS

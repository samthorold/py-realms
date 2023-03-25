from dataclasses import dataclass

from models.enums import Rule


@dataclass
class Action:
    wealth: int = 0
    attack: int = 0
    health: int = 0
    rule: Rule = Rule.ALWAYS

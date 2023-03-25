from models.action import Action
from models.card import Card
from models.enums import ActionType, Faction, Rule, Type

EXPLORER = Card(
    name="explorer",
    type=Type.SHIP,
    faction=Faction.NONE,
    cost=2,
    actions=[
        Action(n=2, type=ActionType.WEALTH, rule=Rule.ALWAYS),
        Action(n=2, type=ActionType.ATTACK, rule=Rule.SCRAP),
    ],
)

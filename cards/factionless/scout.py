from models.action import Action
from models.card import Card
from models.enums import ActionType, Faction, Rule, Type

SCOUT = Card(
    name="scout",
    type=Type.SHIP,
    faction=Faction.NONE,
    cost=0,
    actions=[
        Action(n=1, type=ActionType.WEALTH, rule=Rule.ALWAYS),
    ],
)

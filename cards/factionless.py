from models.action import Action
from models.card import Card
from models.enums import ActionType, Faction, Rule, Type

EXPLORER = Card(
    name="explorer",
    type=Type.SHIP,
    faction=Faction.NONE,
    cost=2,
    actions=[
        Action(n=2, type=ActionType.TRADE, rule=Rule.ALWAYS),
        Action(n=2, type=ActionType.ATTACK, rule=Rule.SCRAP),
    ],
)


SCOUT = Card(
    name="scout",
    type=Type.SHIP,
    faction=Faction.NONE,
    cost=0,
    actions=[
        Action(n=1, type=ActionType.TRADE, rule=Rule.ALWAYS),
    ],
)


VIPER = Card(
    name="viper",
    cost=0,
    type=Type.SHIP,
    faction=Faction.NONE,
    actions=[Action(n=1, type=ActionType.ATTACK, rule=Rule.ALWAYS)],
)

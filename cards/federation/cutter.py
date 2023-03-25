from models.action import Action
from models.card import Card
from models.enums import ActionType, Faction, Rule, Type

CUTTER = Card(
    name="cutter",
    cost=2,
    type=Type.SHIP,
    faction=Faction.IMPERIAL,
    actions=[
        Action(n=2, type=ActionType.WEALTH, rule=Rule.ALWAYS),
        Action(n=4, type=ActionType.HEALTH, rule=Rule.ALWAYS),
        Action(n=4, type=ActionType.ATTACK, rule=Rule.ALLY_IN_PLAY),
    ],
)

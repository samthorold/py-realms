from models.action import Action, ActionType
from models.card import Card
from models.enums import Faction, Rule, Type


BATTLE_BLOB = Card(
    name="battle blob",
    cost=6,
    type=Type.SHIP,
    faction=Faction.BLOB,
    actions=[
        Action(n=8, type=ActionType.ATTACK, rule=Rule.ALWAYS),
        Action(n=1, type=ActionType.DRAW, rule=Rule.ALLY_IN_PLAY),
        Action(n=4, type=ActionType.ATTACK, rule=Rule.SCRAP),
    ],
)


BATTLE_POD = Card(
    name="battle pod",
    cost=2,
    type=Type.SHIP,
    faction=Faction.BLOB,
    actions=[
        Action(n=4, type=ActionType.ATTACK, rule=Rule.ALWAYS),
        Action(n=1, type=ActionType.SCRAP_TRADE, rule=Rule.ALWAYS),
        Action(n=2, type=ActionType.ATTACK, rule=Rule.ALLY_IN_PLAY),
    ],
)


BLOB_CARRIER = Card(
    name="blob carrier",
    cost=6,
    type=Type.SHIP,
    faction=Faction.BLOB,
    actions=[
        Action(n=7, type=ActionType.ATTACK, rule=Rule.ALWAYS),
        Action(n=1, type=ActionType.ACQUIRE_TOP, rule=Rule.ALLY_IN_PLAY),
    ],
)


BLOB_DESTROYER = Card(
    name="blob destroyer",
    cost=4,
    type=Type.SHIP,
    faction=Faction.BLOB,
    actions=[
        Action(n=6, type=ActionType.ATTACK, rule=Rule.ALWAYS),
        Action(n=1, type=ActionType.SCRAP_TRADE, rule=Rule.ALLY_IN_PLAY),
        Action(n=1, type=ActionType.DESTROY_BASE, rule=Rule.ALLY_IN_PLAY),
    ],
)

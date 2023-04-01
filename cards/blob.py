from models.action import Action
from models.card import Card
from models.enums import ActionType, Faction, Rule, CardType


BATTLE_BLOB = Card(
    name="battle blob",
    cost=6,
    type=CardType.SHIP,
    faction=Faction.BLOB,
    actions=(
        Action(n=8, type=ActionType.COMBAT, rule=Rule.ALWAYS),
        Action(n=1, type=ActionType.DRAW, rule=Rule.ALLY),
        Action(n=4, type=ActionType.COMBAT, rule=Rule.SCRAP),
    ),
)


BATTLE_POD = Card(
    name="battle pod",
    cost=2,
    type=CardType.SHIP,
    faction=Faction.BLOB,
    actions=(
        Action(n=4, type=ActionType.COMBAT, rule=Rule.ALWAYS),
        Action(n=1, type=ActionType.SCRAP_TRADE, rule=Rule.ALWAYS),
        Action(n=2, type=ActionType.COMBAT, rule=Rule.ALLY),
    ),
)


BLOB_CARRIER = Card(
    name="blob carrier",
    cost=6,
    type=CardType.SHIP,
    faction=Faction.BLOB,
    actions=(
        Action(n=7, type=ActionType.COMBAT, rule=Rule.ALWAYS),
        Action(n=1, type=ActionType.ACQUIRE_TOP, rule=Rule.ALLY),
    ),
)


BLOB_DESTROYER = Card(
    name="blob destroyer",
    cost=4,
    type=CardType.SHIP,
    faction=Faction.BLOB,
    actions=(
        Action(n=6, type=ActionType.COMBAT, rule=Rule.ALWAYS),
        Action(n=1, type=ActionType.SCRAP_TRADE, rule=Rule.ALLY),
        Action(n=1, type=ActionType.DESTROY_BASE, rule=Rule.ALLY),
    ),
)

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


BLOB_FIGHTER = Card(
    name="blob fighter",
    cost=1,
    type=CardType.SHIP,
    faction=Faction.BLOB,
    actions=(
        Action(n=3, type=ActionType.COMBAT, rule=Rule.ALWAYS),
        Action(n=1, type=ActionType.DRAW, rule=Rule.ALLY),
    ),
)


BLOB_WHEEL = Card(
    name="blob wheel",
    cost=3,
    type=CardType.BASE,
    faction=Faction.BLOB,
    defense=5,
    actions=(
        Action(n=1, type=ActionType.COMBAT, rule=Rule.ALWAYS),
        Action(n=3, type=ActionType.TRADE, rule=Rule.SCRAP),
    ),
)


BLOB_WORLD = Card(
    name="blob world",
    cost=8,
    type=CardType.BASE,
    faction=Faction.BLOB,
    defense=8,  # not in ss interestingly
    actions=(
        Action(
            n=1,
            type=ActionType.COMBAT_5_OR_DRAW_FOR_EACH_BLOB,
            rule=Rule.ALWAYS,
        ),
    ),
)


MOTHERSHIP = Card(
    name="mothership",
    cost=7,
    type=CardType.SHIP,
    faction=Faction.BLOB,
    actions=(
        Action(n=6, type=ActionType.COMBAT, rule=Rule.ALWAYS),
        Action(n=1, type=ActionType.DRAW, rule=Rule.ALWAYS),
        Action(n=1, type=ActionType.DRAW, rule=Rule.ALLY),
    ),
)


RAM = Card(
    name="ram",
    cost=3,
    type=CardType.SHIP,
    faction=Faction.BLOB,
    actions=(
        Action(n=5, type=ActionType.COMBAT, rule=Rule.ALWAYS),
        Action(n=2, type=ActionType.COMBAT, rule=Rule.ALLY),
        Action(n=3, type=ActionType.TRADE, rule=Rule.SCRAP),
    ),
)

HIVE = Card(
    name="the hive",
    cost=5,
    type=CardType.BASE,
    faction=Faction.BLOB,
    defense=5,
    actions=(
        Action(n=3, type=ActionType.COMBAT, rule=Rule.ALWAYS),
        Action(n=1, type=ActionType.DRAW, rule=Rule.ALLY),
    ),
)

TRADE_POD = Card(
    name="trade pod",
    cost=2,
    type=CardType.SHIP,
    faction=Faction.BLOB,
    actions=(
        Action(n=3, type=ActionType.TRADE, rule=Rule.ALWAYS),
        Action(n=2, type=ActionType.COMBAT, rule=Rule.ALLY),
    ),
)

BLOB_DECK = [
    (BATTLE_BLOB, 1),
    (BATTLE_POD, 2),
    (BLOB_CARRIER, 1),
    (BLOB_DESTROYER, 2),
    (BLOB_FIGHTER, 3),
    (BLOB_WHEEL, 3),
    (BLOB_WORLD, 1),
    (MOTHERSHIP, 1),
    (RAM, 2),
    (HIVE, 1),
    (TRADE_POD, 3),
]

from models.action import Action
from models.card import Card
from models.enums import ActionType, Faction, Rule, CardType


BARTER_WORLD = Card(
    name="barter world",
    cost=5,
    defense=4,
    type=CardType.BASE,
    faction=Faction.FEDERATION,
    actions=(
        Action(n=1, type=ActionType.TRADE_2_OR_AUTHORITY_2, rule=Rule.ALWAYS),
        Action(n=5, type=ActionType.COMBAT, rule=Rule.SCRAP),
    ),
)


CENTRAL_OFFICE = Card(
    name="central office",
    cost=7,
    defense=6,
    type=CardType.BASE,
    faction=Faction.FEDERATION,
    actions=(
        Action(n=2, type=ActionType.TRADE, rule=Rule.ALWAYS),
        Action(n=1, type=ActionType.NEXT_SHIP_TOP_OF_DECK, rule=Rule.ALWAYS),
        Action(n=1, type=ActionType.DRAW, rule=Rule.ALLY),
    ),
)


COMMAND_SHIP = Card(
    name="command ship",
    cost=8,
    type=CardType.SHIP,
    faction=Faction.FEDERATION,
    actions=(
        Action(n=4, type=ActionType.AUTHORITY, rule=Rule.ALWAYS),
        Action(n=5, type=ActionType.COMBAT, rule=Rule.ALWAYS),
        Action(n=2, type=ActionType.DRAW, rule=Rule.ALWAYS),
        Action(n=1, type=ActionType.DESTROY_BASE, rule=Rule.ALLY),
    ),
)


CUTTER = Card(
    name="cutter",
    cost=2,
    type=CardType.SHIP,
    faction=Faction.FEDERATION,
    actions=(
        Action(n=2, type=ActionType.TRADE, rule=Rule.ALWAYS),
        Action(n=4, type=ActionType.AUTHORITY, rule=Rule.ALWAYS),
        Action(n=4, type=ActionType.COMBAT, rule=Rule.ALLY),
    ),
)


DEFENSE_CENTER = Card(
    name="defense_center",
    cost=5,
    defense=5,
    type=CardType.OUTPOST,
    faction=Faction.FEDERATION,
    actions=(
        Action(n=2, type=ActionType.COMBAT_2_OR_AUTHORITY_3, rule=Rule.ALWAYS),
        Action(n=2, type=ActionType.COMBAT, rule=Rule.ALLY),
    ),
)


EMBASSY_YACHT = Card(
    name="embassy yacht",
    cost=3,
    type=CardType.SHIP,
    faction=Faction.FEDERATION,
    actions=(
        Action(n=2, type=ActionType.TRADE, rule=Rule.ALWAYS),
        Action(n=3, type=ActionType.AUTHORITY, rule=Rule.ALWAYS),
        Action(n=2, type=ActionType.DRAW, rule=Rule.BASES_IN_PLAY_2),
    ),
)


FEDERATION_SHUTTLE = Card(
    name="federation shuttle",
    cost=1,
    type=CardType.SHIP,
    faction=Faction.FEDERATION,
    actions=(
        Action(n=2, type=ActionType.TRADE, rule=Rule.ALWAYS),
        Action(n=4, type=ActionType.AUTHORITY, rule=Rule.ALLY),
    ),
)

FLAGSHIP = Card(
    name="flagship",
    cost=6,
    type=CardType.SHIP,
    faction=Faction.FEDERATION,
    actions=(
        Action(n=5, type=ActionType.COMBAT, rule=Rule.ALWAYS),
        Action(n=1, type=ActionType.DRAW, rule=Rule.ALWAYS),
        Action(n=5, type=ActionType.AUTHORITY, rule=Rule.ALLY),
    ),
)

FREIGHTER = Card(
    name="freighter",
    cost=4,
    type=CardType.SHIP,
    faction=Faction.FEDERATION,
    actions=(
        Action(n=4, type=ActionType.TRADE, rule=Rule.ALWAYS),
        Action(n=5, type=ActionType.NEXT_SHIP_TOP_OF_DECK, rule=Rule.ALLY),
    ),
)


PORT_OF_CALL = Card(
    name="port of call",
    cost=6,
    defense=6,
    type=CardType.OUTPOST,
    faction=Faction.FEDERATION,
    actions=(
        Action(n=3, type=ActionType.TRADE, rule=Rule.ALWAYS),
        Action(n=1, type=ActionType.DRAW_AND_DESTROY_TARGET_BASE, rule=Rule.SCRAP),
    ),
)

TRADE_ESCORT = Card(
    name="trade escort",
    cost=5,
    type=CardType.SHIP,
    faction=Faction.FEDERATION,
    actions=(
        Action(n=4, type=ActionType.COMBAT, rule=Rule.ALWAYS),
        Action(n=4, type=ActionType.AUTHORITY, rule=Rule.ALWAYS),
        Action(n=1, type=ActionType.DRAW, rule=Rule.ALLY),
    ),
)


TRADE_POST = Card(
    name="trade post",
    cost=3,
    defense=4,
    type=CardType.OUTPOST,
    faction=Faction.FEDERATION,
    actions=(
        Action(n=1, type=ActionType.AUTHORITY_1_OR_TRADE_1, rule=Rule.ALWAYS),
        Action(n=3, type=ActionType.COMBAT, rule=Rule.SCRAP),
    ),
)


FEDERATION_DECK = [
    (BARTER_WORLD, 2),
    (CENTRAL_OFFICE, 1),
    (COMMAND_SHIP, 1),
    (CUTTER, 3),
    (DEFENSE_CENTER, 1),
    (EMBASSY_YACHT, 2),
    (FEDERATION_SHUTTLE, 3),
    (FLAGSHIP, 1),
    (FREIGHTER, 2),
    (PORT_OF_CALL, 1),
    (TRADE_ESCORT, 1),
    (TRADE_POST, 2),
]

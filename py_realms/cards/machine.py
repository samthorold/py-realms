from py_realms.models.action import Action
from py_realms.models.card import Card
from py_realms.models.enums import ActionType, Faction, Rule, CardType


BATTLE_MECH = Card(
    name="battle mech",
    type=CardType.SHIP,
    faction=Faction.MACHINE,
    cost=5,
    actions=(
        Action(type=ActionType.COMBAT, n=4, rule=Rule.ALWAYS),
        Action(type=ActionType.SCRAP_HAND_OR_DISCARD, n=1, rule=Rule.ALWAYS),
        Action(type=ActionType.DRAW, n=1, rule=Rule.ALLY),
    ),
)


BATTLE_STATION = Card(
    name="battle station",
    cost=1,
    type=CardType.OUTPOST,
    faction=Faction.MACHINE,
    defense=5,
    actions=(Action(n=5, type=ActionType.COMBAT, rule=Rule.SCRAP),),
)


BRAIN_WORLD = Card(
    name="brain world",
    cost=8,
    type=CardType.OUTPOST,
    faction=Faction.MACHINE,
    defense=6,
    actions=(
        Action(
            type=ActionType.SCRAP_HAND_OR_DISCARD_THEN_DRAW,
            n=2,
            rule=Rule.ALWAYS,
        ),
    ),
)


JUNKYARD = Card(
    name="junkyard",
    cost=6,
    type=CardType.OUTPOST,
    faction=Faction.MACHINE,
    defense=5,
    actions=(
        Action(
            type=ActionType.SCRAP_HAND_OR_DISCARD,
            n=1,
            rule=Rule.ALWAYS,
        ),
    ),
)


MACHINE_BASE = Card(
    name="machine base",
    cost=7,
    type=CardType.OUTPOST,
    faction=Faction.MACHINE,
    defense=6,
    actions=(
        Action(
            type=ActionType.DRAW_THEN_SCRAP_FROM_HAND,
            n=1,
            rule=Rule.ALWAYS,
        ),
    ),
)


MECH_WORLD = Card(
    name="mech world",
    cost=5,
    type=CardType.OUTPOST,
    faction=Faction.ALL,
    actions=tuple(),
    defense=6,
)


MISSILE_BOT = Card(
    name="missile bot",
    cost=2,
    type=CardType.SHIP,
    faction=Faction.MACHINE,
    actions=(
        Action(type=ActionType.SCRAP_HAND_OR_DISCARD, n=1, rule=Rule.ALWAYS),
        Action(type=ActionType.COMBAT, n=2, rule=Rule.ALLY),
    ),
)


MISSILE_MECH = Card(
    name="missile mech",
    cost=6,
    type=CardType.SHIP,
    faction=Faction.MACHINE,
    actions=(
        Action(type=ActionType.COMBAT, n=6, rule=Rule.ALWAYS),
        Action(type=ActionType.DESTROY_BASE, n=1, rule=Rule.ALWAYS),
        Action(type=ActionType.DRAW, n=1, rule=Rule.ALLY),
    ),
)


PATROL_MECH = Card(
    name="patrol mech",
    cost=4,
    type=CardType.SHIP,
    faction=Faction.MACHINE,
    actions=(
        Action(type=ActionType.TRADE_3_OR_COMBAT_5, n=1, rule=Rule.ALWAYS),
        Action(type=ActionType.SCRAP_HAND_OR_DISCARD, n=1, rule=Rule.ALLY),
    ),
)


STEALTH_NEEDLE = Card(
    name="stealth needle",
    cost=4,
    type=CardType.SHIP,
    faction=Faction.MACHINE,
    actions=(Action(type=ActionType.COPY_CARD, n=1, rule=Rule.ALWAYS),),
)


SUPPLY_BOT = Card(
    name="supply bot",
    cost=3,
    type=CardType.SHIP,
    faction=Faction.MACHINE,
    actions=(
        Action(type=ActionType.TRADE, n=2, rule=Rule.ALLY),
        Action(type=ActionType.SCRAP_HAND_OR_DISCARD, n=1, rule=Rule.ALWAYS),
        Action(type=ActionType.COMBAT, n=2, rule=Rule.ALLY),
    ),
)


TRADE_BOT = Card(
    name="trade bot",
    cost=1,
    type=CardType.SHIP,
    faction=Faction.MACHINE,
    actions=(
        Action(type=ActionType.TRADE, n=1, rule=Rule.ALLY),
        Action(type=ActionType.SCRAP_HAND_OR_DISCARD, n=1, rule=Rule.ALWAYS),
        Action(type=ActionType.COMBAT, n=2, rule=Rule.ALLY),
    ),
)


MACHINE_DECK = [
    (BATTLE_MECH, 1),
    (BATTLE_STATION, 2),
    (BRAIN_WORLD, 1),
    (JUNKYARD, 1),
    (MACHINE_BASE, 1),
    (MECH_WORLD, 1),
    (MISSILE_BOT, 3),
    (MISSILE_MECH, 1),
    (PATROL_MECH, 2),
    (STEALTH_NEEDLE, 1),
    (SUPPLY_BOT, 3),
    (TRADE_BOT, 3),
]

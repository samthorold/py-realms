from models.action import Action
from models.card import Card
from models.enums import ActionType, CardType, Faction, Rule


BATTLECRUISER = Card(
    name="battlecruiser",
    type=CardType.SHIP,
    faction=Faction.IMPERIAL,
    cost=6,
    actions=(
        Action(type=ActionType.COMBAT, n=5, rule=Rule.ALWAYS),
        Action(type=ActionType.DRAW, n=1, rule=Rule.ALWAYS),
        Action(type=ActionType.OPPONENT_DISCARD, n=1, rule=Rule.ALLY),
        Action(type=ActionType.DRAW_AND_DESTROY_TARGET_BASE, n=1, rule=Rule.SCRAP),
    ),
)


CORVETTE = Card(
    name="corvette",
    type=CardType.SHIP,
    faction=Faction.IMPERIAL,
    cost=2,
    actions=(
        Action(type=ActionType.COMBAT, n=1, rule=Rule.ALWAYS),
        Action(type=ActionType.DRAW, n=1, rule=Rule.ALWAYS),
        Action(type=ActionType.COMBAT, n=2, rule=Rule.ALLY),
    ),
)


DREADNAUGHT = Card(
    name="dreadnaught",
    type=CardType.SHIP,
    faction=Faction.IMPERIAL,
    cost=7,
    actions=(
        Action(type=ActionType.COMBAT, n=7, rule=Rule.ALWAYS),
        Action(type=ActionType.DRAW, n=1, rule=Rule.ALWAYS),
        Action(type=ActionType.COMBAT, n=5, rule=Rule.SCRAP),
    ),
)


FLEET_HQ = Card(
    name="fleet hq",
    type=CardType.BASE,
    faction=Faction.IMPERIAL,
    cost=8,
    defense=8,
    actions=(Action(type=ActionType.COMBAT_ON_PLAY_SHIP, n=1, rule=Rule.ALWAYS),),
)


IMPERIAL_FIGHTER = Card(
    name="imperial fighter",
    type=CardType.SHIP,
    faction=Faction.IMPERIAL,
    cost=3,
    actions=(
        Action(type=ActionType.COMBAT, n=2, rule=Rule.ALWAYS),
        Action(type=ActionType.OPPONENT_DISCARD, n=1, rule=Rule.ALWAYS),
        Action(type=ActionType.COMBAT, n=2, rule=Rule.ALLY),
    ),
)


IMPERIAL_FRIGATE = Card(
    name="imperial frigate",
    type=CardType.SHIP,
    faction=Faction.IMPERIAL,
    cost=3,
    actions=(
        Action(type=ActionType.COMBAT, n=4, rule=Rule.ALWAYS),
        Action(type=ActionType.OPPONENT_DISCARD, n=1, rule=Rule.ALWAYS),
        Action(type=ActionType.COMBAT, n=2, rule=Rule.ALLY),
        Action(type=ActionType.DRAW, n=1, rule=Rule.SCRAP),
    ),
)


RECYCLING_STATION = Card(
    name="recycling station",
    type=CardType.OUTPOST,
    faction=Faction.IMPERIAL,
    cost=4,
    defense=4,
    actions=(Action(type=ActionType.DISCARD_THEN_DRAW, n=2, rule=Rule.ALWAYS),),
)


ROYAL_REDOUBT = Card(
    name="royal redoubt",
    type=CardType.OUTPOST,
    faction=Faction.IMPERIAL,
    cost=6,
    defense=6,
    actions=(
        Action(type=ActionType.COMBAT, n=3, rule=Rule.ALWAYS),
        Action(type=ActionType.OPPONENT_DISCARD, n=1, rule=Rule.ALLY),
    ),
)


SPACE_STATION = Card(
    name="space station",
    type=CardType.OUTPOST,
    faction=Faction.IMPERIAL,
    cost=4,
    defense=4,
    actions=(
        Action(type=ActionType.COMBAT, n=2, rule=Rule.ALWAYS),
        Action(type=ActionType.COMBAT, n=2, rule=Rule.ALLY),
        Action(type=ActionType.TRADE, n=4, rule=Rule.SCRAP),
    ),
)


SURVEY_SHIP = Card(
    name="survey ship",
    type=CardType.SHIP,
    faction=Faction.IMPERIAL,
    cost=4,
    actions=(
        Action(type=ActionType.DRAW, n=1, rule=Rule.ALWAYS),
        Action(type=ActionType.OPPONENT_DISCARD, n=1, rule=Rule.SCRAP),
    ),
)


WAR_WORLD = Card(
    name="war world",
    type=CardType.OUTPOST,
    faction=Faction.IMPERIAL,
    cost=5,
    defense=4,
    actions=(
        Action(type=ActionType.COMBAT, n=3, rule=Rule.ALWAYS),
        Action(type=ActionType.COMBAT, n=4, rule=Rule.ALLY),
    ),
)


IMPERIAL_DECK = [
    (BATTLECRUISER, 1),
    (CORVETTE, 2),
    (DREADNAUGHT, 1),
    (FLEET_HQ, 1),
    (IMPERIAL_FIGHTER, 3),
    (IMPERIAL_FRIGATE, 3),
    (RECYCLING_STATION, 2),
    (ROYAL_REDOUBT, 1),
    (SPACE_STATION, 2),
    (SURVEY_SHIP, 3),
    (WAR_WORLD, 1),
]

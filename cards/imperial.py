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
        Action(
            type=ActionType.DRAW_AND_DESTROY_TARGET_BASE, n=1, rule=Rule.SCRAP
        ),
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
    actions=(
        Action(type=ActionType.COMBAT_ON_PLAY_SHIP, n=1, rule=Rule.ALWAYS),
    ),
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

from models.action import Action
from models.card import Card
from models.enums import ActionType, Faction, Rule, CardType


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

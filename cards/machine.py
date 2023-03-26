from models.action import Action
from models.card import Card
from models.enums import ActionType, Faction, Rule, CardType


BATTLE_STATION = Card(
    name="battle station",
    cost=1,
    type=CardType.OUTPOST,
    faction=Faction.MACHINE,
    defense=5,
    actions=(Action(n=5, type=ActionType.COMBAT, rule=Rule.SCRAP),),
)

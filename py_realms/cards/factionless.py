from py_realms.models.action import Action
from py_realms.models.card import Card
from py_realms.models.enums import ActionType, Faction, Rule, CardType

EXPLORER = Card(
    name="explorer",
    type=CardType.SHIP,
    faction=Faction.NONE,
    cost=2,
    actions=(
        Action(n=2, type=ActionType.TRADE, rule=Rule.ALWAYS),
        Action(n=2, type=ActionType.COMBAT, rule=Rule.SCRAP),
    ),
)


SCOUT = Card(
    name="scout",
    type=CardType.SHIP,
    faction=Faction.NONE,
    cost=0,
    actions=(Action(n=1, type=ActionType.TRADE, rule=Rule.ALWAYS),),
)


VIPER = Card(
    name="viper",
    cost=0,
    type=CardType.SHIP,
    faction=Faction.NONE,
    actions=(Action(n=1, type=ActionType.COMBAT, rule=Rule.ALWAYS),),
)

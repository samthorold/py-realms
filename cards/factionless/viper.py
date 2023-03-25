from models.action import Action
from models.card import Card
from models.enums import ActionType, Faction, Rule, Type

VIPER = Card(
    name="viper",
    cost=0,
    type=Type.SHIP,
    faction=Faction.NONE,
    actions=[Action(n=1, type=ActionType.ATTACK, rule=Rule.ALWAYS)],
)

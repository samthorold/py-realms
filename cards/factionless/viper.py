from models.action import Action
from models.card import Card
from models.enums import Faction, Type

VIPER = Card(
    name="viper",
    cost=0,
    type=Type.SHIP,
    faction=Faction.NONE,
    actions=[Action(attack=1)],
)

from models.card import Card
from models.enums import Faction, Type

SCOUT = Card(
    name="scout",
    type=Type.SHIP,
    faction=Faction.NONE,
    cost=0,
    money=1,
    actions=[],
)

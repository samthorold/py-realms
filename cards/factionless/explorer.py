from models.action import Action
from models.card import Card
from models.enums import Faction, Rule, Type

EXPLORER = Card(
    name="explorer",
    type=Type.SHIP,
    faction=Faction.NONE,
    cost=2,
    money=2,
    actions=[Action(attack=2, rule=Rule.SCRAP)],
)

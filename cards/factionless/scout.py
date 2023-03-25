from models.action import Action
from models.card import Card
from models.enums import Faction, Rule, Type

SCOUT = Card(
    name="scout",
    type=Type.SHIP,
    faction=Faction.NONE,
    cost=0,
    actions=[
        Action(wealth=1, rule=Rule.ALWAYS),
    ],
)

from models.action import Action
from models.card import Card
from models.enums import Faction, Rule, Type

CUTTER = Card(
    name="cutter",
    cost=2,
    type=Type.SHIP,
    faction=Faction.IMPERIAL,
    actions=[
        Action(wealth=2, rule=Rule.ALWAYS),
        Action(health=4, rule=Rule.ALWAYS),
        Action(attack=4, rule=Rule.ALLY_IN_PLAY),
    ],
)

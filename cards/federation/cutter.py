from models.action import Action
from models.card import Card
from models.enums import Faction, Rule, Type

CUTTER = Card(
    name="cutter",
    cost=2,
    type=Type.SHIP,
    faction=Faction.IMPERIAL,
    money=2,
    actions=[
        Action(health=4),
        Action(attack=4, rule=Rule.SAME_FACTION_IN_PLAY),
    ],
)
from models.action import Action
from models.card import Card
from models.enums import Faction, Rule, Type

EXPLORER = Card(
    name="explorer",
    type=Type.SHIP,
    faction=Faction.NONE,
    cost=2,
    actions=[Action(wealth=2, rule=Rule.ALWAYS), Action(attack=2, rule=Rule.SCRAP)],
)

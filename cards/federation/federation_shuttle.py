from models.action import Action
from models.card import Card
from models.enums import Faction, Rule, Type


FEDERATION_SHUTTLE = Card(
    name="federation shuttle",
    cost=1,
    type=Type.SHIP,
    faction=Faction.IMPERIAL,
    money=2,
    actions=[
        Action(health=4, rule=Rule.ALLY_IN_PLAY),
    ],
)

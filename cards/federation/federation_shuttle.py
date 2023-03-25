from models.action import Action
from models.card import Card
from models.enums import ActionType, Faction, Rule, Type


FEDERATION_SHUTTLE = Card(
    name="federation shuttle",
    cost=1,
    type=Type.SHIP,
    faction=Faction.IMPERIAL,
    actions=[
        Action(n=2, type=ActionType.WEALTH, rule=Rule.ALWAYS),
        Action(n=4, type=ActionType.HEALTH, rule=Rule.ALLY_IN_PLAY),
    ],
)

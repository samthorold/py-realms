from models.action import Action
from models.card import Card
from models.enums import ActionType, Faction, Rule, Type


FEDERATION_SHUTTLE = Card(
    name="federation shuttle",
    cost=1,
    type=Type.SHIP,
    faction=Faction.IMPERIAL,
    actions=(
        Action(n=2, type=ActionType.TRADE, rule=Rule.ALWAYS),
        Action(n=4, type=ActionType.AUTHORITY, rule=Rule.ALLY_IN_PLAY),
    ),
)

CUTTER = Card(
    name="cutter",
    cost=2,
    type=Type.SHIP,
    faction=Faction.IMPERIAL,
    actions=(
        Action(n=2, type=ActionType.TRADE, rule=Rule.ALWAYS),
        Action(n=4, type=ActionType.AUTHORITY, rule=Rule.ALWAYS),
        Action(n=4, type=ActionType.COMBAT, rule=Rule.ALLY_IN_PLAY),
    ),
)

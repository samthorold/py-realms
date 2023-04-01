from models.action import Action
from models.card import Card
from models.enums import ActionType, Faction, Rule, CardType


FEDERATION_SHUTTLE = Card(
    name="federation shuttle",
    cost=1,
    type=CardType.SHIP,
    faction=Faction.FEDERATION,
    actions=(
        Action(n=2, type=ActionType.TRADE, rule=Rule.ALWAYS),
        Action(n=4, type=ActionType.AUTHORITY, rule=Rule.ALLY),
    ),
)

CUTTER = Card(
    name="cutter",
    cost=2,
    type=CardType.SHIP,
    faction=Faction.FEDERATION,
    actions=(
        Action(n=2, type=ActionType.TRADE, rule=Rule.ALWAYS),
        Action(n=4, type=ActionType.AUTHORITY, rule=Rule.ALWAYS),
        Action(n=4, type=ActionType.COMBAT, rule=Rule.ALLY),
    ),
)

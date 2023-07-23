from py_realms.models.action import Action
from py_realms.models.enums import ActionType, Rule


def test_action_as_always() -> None:
    action = Action(
        type=ActionType.PLAY,
        n=1,
        rule=Rule.ALLY,
    )
    got = action.as_always()
    assert got.rule == Rule.ALWAYS
    assert action.type == got.type

import pytest
from models.exceptions import UnknownActionType
from models.game import Game


def test_game_init() -> None:
    game = Game()
    assert len(game._players) == 2


def test_play() -> None:
    game = Game()
    game.action("START_GAME")
    game.action("play", idx=0)
    pl = game.get_current_player()
    assert len(pl._hand) < 5
    assert len(pl._in_play) > 0


def test_unknown_action() -> None:
    game = Game()
    with pytest.raises(UnknownActionType):
        game.action("nigel thornberry")

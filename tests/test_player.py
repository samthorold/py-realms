import pytest

from cards.machine.battle_station import BATTLE_STATION
from models.player import Player


@pytest.fixture
def player() -> Player:
    return Player("")


@pytest.fixture
def player_with_bases() -> Player:
    player = Player("")
    player.hand.append(BATTLE_STATION)
    return player


def test_player_draw(player: Player) -> None:
    player.draw()


def test_player_new_hand(player: Player) -> None:
    player.new_hand()
    assert len(player.hand) == 5


def test_player_new_hand_bases_in_play(player_with_bases: Player) -> None:
    player_with_bases.new_hand()
    assert len(player_with_bases.hand) > 5

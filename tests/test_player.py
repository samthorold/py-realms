import pytest

from py_realms.cards.deck import PLAYER_STARTING_DECK
from py_realms.cards.machine import BATTLE_STATION
from py_realms.models.player import Player


@pytest.fixture
def player() -> Player:
    player = Player(name="", deck=list(PLAYER_STARTING_DECK))
    player.new_hand()
    return player


@pytest.fixture
def player_with_bases(player: Player) -> Player:
    player.in_play.append(BATTLE_STATION)
    return player


def test_player_draw(player: Player) -> None:
    og_hand = len(player.hand)
    og_deck = len(player.deck)
    player.draw()
    assert len(player.hand) > og_hand
    assert len(player.deck) < og_deck


def test_player_new_hand(player: Player) -> None:
    player.new_hand()
    assert len(player.hand) == 5


def test_player_new_hand_bases_in_play(player_with_bases: Player) -> None:
    player_with_bases.new_hand()
    assert len(player_with_bases.hand) == 5

import pytest

from cards.factionless import SCOUT, VIPER
from models.card import Card
from models.exceptions import UnknownActionType
from models.game import Game
from models.player import Player


def test_game_init() -> None:
    game = Game()
    assert len(game._players) == 2


@pytest.mark.parametrize(
    "hand",
    (
        [SCOUT] * 3,
        [SCOUT] * 2 + [VIPER],
        [SCOUT] + [VIPER] * 2,
        [VIPER] * 3,
        [VIPER] * 2 + [SCOUT],
        [VIPER] + [SCOUT] * 2,
    ),
)
def test_play(hand: list[Card] | None) -> None:
    """Play action updates game state as expected.

    - One less card in hand.
    - One more card in play.
    - Card actions added to game actions.

    """

    players = (Player("", hand=hand), Player(""))

    game = Game(players=players)
    game.action("START_GAME")
    pl = game.get_current_player()

    # grab the player's hand before the action
    og_hand = list(pl.hand)
    og_in_play = list(pl.in_play)

    # get the card they are about to play
    card = pl.hand[0]

    # get the count of that card pre-action
    og_hand_count = len([c for c in og_hand if c == card])
    og_in_play_count = len([c for c in og_in_play if c == card])

    # perform the action
    game.action("play", idx=0)

    # get the player's hand after the action
    new_hand_count = len([c for c in pl.hand if c == card])
    new_in_play_count = len([c for c in pl.in_play if c == card])

    # check state
    # TODO: fails when card is a viper
    assert len(pl.hand) < 3 and new_hand_count == (og_hand_count - 1), card
    assert len(pl.in_play) > 0 and new_in_play_count == (
        og_in_play_count + 1
    ), card
    assert all(c in game._actions for c in card.actions), card.actions


def test_unknown_action() -> None:
    game = Game()
    with pytest.raises(UnknownActionType):
        game.action("nigel thornberry")

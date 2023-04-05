import pytest
from models.exceptions import UnknownActionType
from models.game import Game


def test_game_init() -> None:
    game = Game()
    assert len(game._players) == 2


def test_play() -> None:
    """Play action updates game state as expected.

    - One less card in hand.
    - One more card in play.
    - Card actions added to game actions.

    """

    game = Game()
    game.action("START_GAME")
    pl = game.get_current_player()

    # grab the player's hand before the action
    og_hand = list(pl._hand)
    og_in_play = list(pl._in_play)

    # get the card they are about to play
    card = pl._hand[0]

    # get the count of that card pre-action
    og_hand_count = len([c for c in og_hand if c == card])
    og_in_play_count = len([c for c in og_in_play if c == card])

    # perform the action
    game.action("play", idx=0)

    # get the player's hand after the action
    new_hand_count = len([c for c in pl._hand if c == card])
    new_in_play_count = len([c for c in pl._in_play if c == card])

    # check state
    # TODO: fails when card is a viper
    assert len(pl._hand) < 3 and new_hand_count == (og_hand_count - 1), card
    assert len(pl._in_play) > 0 and new_in_play_count == (og_in_play_count + 1), card
    assert all(c in game._actions for c in card.actions), card.actions


def test_unknown_action() -> None:
    game = Game()
    with pytest.raises(UnknownActionType):
        game.action("nigel thornberry")

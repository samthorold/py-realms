import pytest

from py_realms.cards.deck import GAME_STARTING_DECK
from py_realms.cards.factionless import SCOUT, VIPER
from py_realms.models.action import Action
from py_realms.models.card import Card
from py_realms.models.deck import NUM_CARDS_TRADE_DECK, Deck
from py_realms.models.enums import ActionType, Rule
from py_realms.models.exceptions import UnknownActionType
from py_realms.models.game import (
    Game,
    player_setup,
    NUM_CARDS_START_GAME,
    NUM_CARDS_START_TURN,
)
from py_realms.models.player import Player


def test_player_setup() -> None:
    got = player_setup("")
    assert isinstance(got, Player)
    assert len(got.deck) == 10
    assert not got.hand
    assert not got.in_play


def test_game_init() -> None:
    game = Game()
    assert len(game.players) == 2


def test_action_start_game() -> None:
    """Start game action updates game state as expected.

    - Three play actions.
    """

    expected = [
        Action(type=ActionType.PLAY, n=1, rule=Rule.ALWAYS)
    ] * NUM_CARDS_START_GAME
    game = Game()
    game.action(Action(type=ActionType.START_GAME, n=NUM_CARDS_START_GAME))
    assert game.actions == expected


def test_action_start_turn() -> None:
    """Start turn action updates game state as expected.

    - Five play actions.
    """

    expected = [
        Action(type=ActionType.PLAY, n=1, rule=Rule.ALWAYS)
    ] * NUM_CARDS_START_TURN
    game = Game(actions=[Action(type=ActionType.START_TURN, n=NUM_CARDS_START_TURN)])
    game.action(Action(type=ActionType.START_TURN, n=NUM_CARDS_START_TURN))
    assert game.actions == expected


def test_action_acquire() -> None:
    """Acquire action updates game state as expected.

    - Player's discard pile contains the acquired card.
    - Player's trade reduced by cost of the acquired card.
    - Trade row no longer contains the acquired card.
    - Trade row contains five cards.
    """

    starting_trade = 100
    acquire_idx = 0

    players = (
        Player(name="", trade=starting_trade),
        Player(name=""),
    )
    actions = [Action(type=ActionType.ACQUIRE)]
    game = Game(players=players, actions=actions)
    pl = game.get_current_player()
    card = game.deck.trade_row[acquire_idx]
    # may draw the same card again from the trade deck
    # so count of acquired card in the trade row will be the same.
    og_count = len([c for c in game.deck.trade_row + game.deck.trade_deck if c == card])

    assert card not in pl.discard_pile

    game.action("acquire", acquire_idx)

    assert pl.discard_pile[-1] == card
    assert pl.trade == (starting_trade - card.cost)

    new_count = len(
        [c for c in game.deck.trade_row + game.deck.trade_deck if c == card]
    )
    assert new_count == (og_count - 1)
    assert len(game.deck.trade_row) == NUM_CARDS_TRADE_DECK


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
def test_action_play(hand: list[Card]) -> None:
    """Play action updates game state as expected.

    - One less card in hand.
    - One more card in play.
    - Card actions added to game actions.

    """

    players = (Player(name="", hand=hand), Player(name=""))

    game = Game(deck=Deck(trade_deck=list(GAME_STARTING_DECK)), players=players)
    game.action(Action(type=ActionType.START_GAME, n=NUM_CARDS_START_GAME))
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
    assert len(pl.hand) < NUM_CARDS_START_GAME and new_hand_count == (
        og_hand_count - 1
    ), card
    assert len(pl.in_play) > 0 and new_in_play_count == (og_in_play_count + 1), card
    assert all(c in game.actions for c in card.actions), card.actions


def test_unknown_action() -> None:
    game = Game()
    with pytest.raises(UnknownActionType):
        game.action("nigel thornberry")

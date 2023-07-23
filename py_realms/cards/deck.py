from py_realms.cards.blob import BLOB_DECK
from py_realms.cards.factionless import SCOUT, VIPER
from py_realms.cards.federation import FEDERATION_DECK
from py_realms.cards.imperial import IMPERIAL_DECK
from py_realms.cards.machine import MACHINE_DECK
from py_realms.models.card import Card


PLAYER_STARTING_DECK = tuple([VIPER] * 2 + [SCOUT] * 8)


game_starting_deck = BLOB_DECK + FEDERATION_DECK + IMPERIAL_DECK + MACHINE_DECK

GAME_STARTING_DECK: tuple[Card, ...] = tuple()
for card, n in game_starting_deck:
    for _ in range(n):
        GAME_STARTING_DECK += (card,)

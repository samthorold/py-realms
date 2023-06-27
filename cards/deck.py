from cards.blob import BLOB_DECK
from cards.factionless import SCOUT, VIPER
from cards.federation import FEDERATION_DECK
from cards.imperial import IMPERIAL_DECK
from cards.machine import MACHINE_DECK
from models.card import Card


PLAYER_STARTING_DECK = tuple([VIPER] * 2 + [SCOUT] * 8)


game_starting_deck = BLOB_DECK + FEDERATION_DECK + IMPERIAL_DECK + MACHINE_DECK

GAME_STARTING_DECK: tuple[Card, ...] = tuple()
for card, n in game_starting_deck:
    for _ in range(n):
        GAME_STARTING_DECK += (card,)

from cards.blob import BATTLE_BLOB, BATTLE_POD, BLOB_CARRIER, BLOB_DESTROYER
from cards.factionless import SCOUT, VIPER
from cards.federation import CUTTER, FEDERATION_SHUTTLE
from cards.machine import (
    BATTLE_MECH,
    BATTLE_STATION,
    BRAIN_WORLD,
    JUNKYARD,
    MACHINE_BASE,
    MECH_WORLD,
    MISSILE_BOT,
    MISSILE_MECH,
    PATROL_MECH,
    STEALTH_NEEDLE,
    SUPPLY_BOT,
    TRADE_BOT,
)
from models.card import Card


PLAYER_STARTING_DECK = tuple([VIPER] * 2 + [SCOUT] * 8)


game_starting_deck = [
    (BATTLE_BLOB, 1),
    (BATTLE_POD, 2),
    (BLOB_CARRIER, 1),
    (BLOB_DESTROYER, 2),
    # [BLOB_FIGHTER] * 3 +
    # [BLOB_WHEEL] * 3 +
    # [BLOB_WORLD] * 1 +
    # [MOTHERSHIP] * 1 +
    (BATTLE_MECH, 1),
    (BATTLE_STATION, 2),
    (BRAIN_WORLD, 1),
    (JUNKYARD, 1),
    (MACHINE_BASE, 1),
    (MECH_WORLD, 1),
    (MISSILE_BOT, 3),
    (MISSILE_MECH, 1),
    (PATROL_MECH, 2),
    (STEALTH_NEEDLE, 1),
    (SUPPLY_BOT, 3),
    (TRADE_BOT, 3),
    (CUTTER, 4),
    (FEDERATION_SHUTTLE, 4),
]

GAME_STARTING_DECK: tuple[Card, ...] = tuple()
for card, n in game_starting_deck:
    for _ in range(n):
        GAME_STARTING_DECK += (card,)

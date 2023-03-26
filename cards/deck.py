from cards.blob import BATTLE_BLOB, BATTLE_POD, BLOB_CARRIER, BLOB_DESTROYER
from cards.factionless import SCOUT, VIPER
from cards.federation import CUTTER, FEDERATION_SHUTTLE


PLAYER_STARTING_DECK = tuple([VIPER] * 2 + [SCOUT] * 8)


GAME_STARTING_DECK = tuple(
    [BATTLE_BLOB] * 1
    + [BATTLE_POD] * 2
    + [BLOB_CARRIER] * 1
    + [BLOB_DESTROYER] * 2
    +
    # [BLOB_FIGHTER] * 3 +
    # [BLOB_WHEEL] * 3 +
    # [BLOB_WORLD] * 1 +
    # [MOTHERSHIP] * 1 +
    [CUTTER] * 4
    + [FEDERATION_SHUTTLE] * 4
)

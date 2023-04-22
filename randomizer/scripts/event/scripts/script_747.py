# pylint: disable=C0301

"""E0747_MUSHROOM_KINGDOM_INN_2F_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ApplyTileModToLevel(
            use_alternate=True, room_id=R052_MUSHROOM_KINGDOM_INN_2F, mod_id=1
        ),
        JmpIfBitSet(OCCUPIED_MUSHROOM_KINGDOM_INN, ["EVENT_256_ret_0"]),
        JmpIfBitSet(MUSHROOM_KINGDOM_INN, ["EVENT_256_ret_0"]),
        JmpIfBitSet(TEMP_7042_7, ["EVENT_256_ret_0"]),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)

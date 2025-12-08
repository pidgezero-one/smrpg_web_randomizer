# pylint: disable=C0301

"""E3814_MUSHROOM_KINGDOM_LIBERATED_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(TEMP_7042_7),
        JmpIfBitSet(
            MUSHROOM_KINGDOM_LIBERATED, ["EVENT_3814_remove_from_current_level_5"]
        ),
        FadeInFromBlack(sync=False),
        Return(),
        RemoveObjectFromCurrentLevel(
            NPC_0, identifier="EVENT_3814_remove_from_current_level_5"
        ),
        SummonObjectToCurrentLevel(NPC_1),
        SetSyncActionScript(NPC_1, A0119_SLOW_SEQUENCE_LOOP),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[ASTransferXYZFPixels(x=6, y=250, z=0, direction=EAST)]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R022_MUSHROOM_KINGDOM_CASTLE_GUEST_ROOM,
            mod_id=0),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)

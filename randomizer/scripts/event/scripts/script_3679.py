# E3679_NIMBUS_CASTLE_EGG_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_6,
            R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM,
            ["EVENT_3679_action_queue_sync_5"],
        ),
        ApplySolidityModToLevel(
            permanent=True, room_id=R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, mod_id=0
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASTransferToXYZF(x=20, y=49, z=10, direction=EAST),
                ASSetSpriteSequence(index=6, is_sequence=True, looping=True),
            ],
            identifier="EVENT_3679_action_queue_sync_5",
        ),
        RememberLastObject(),
        SetSyncActionScript(NPC_1, A0978_RANDOMLY_FACE_SOUTHWEST),
        JmpIfBitClear(
            NIMBUS_MID_BOSS_COMPLETED, ["EVENT_3679_fade_in_from_black_async_12"]
        ),
        FadeInFromBlack(
            sync=False, identifier="EVENT_3679_fade_in_from_black_async_12"
        ),
        Return(),
    ]
)

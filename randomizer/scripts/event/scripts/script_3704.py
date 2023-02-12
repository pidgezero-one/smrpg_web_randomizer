# E3704_NIMBUS_CASTLE_OCCUPIED_5_DOOR_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            mod_id=0,
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_9,
            R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            ["EVENT_3704_jmp_if_object_in_level_3"],
        ),
        ActionQueueAsync(
            target=NPC_9,
            subscript=[
                ASTransferXYZFPixels(x=244, y=250, z=0, direction=EAST),
                ASSetPriority(3),
            ],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_1,
            R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            ["EVENT_3704_jmp_if_object_in_level_7"],
            identifier="EVENT_3704_jmp_if_object_in_level_3",
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_3,
            R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            ["EVENT_3704_jmp_if_object_in_level_7"],
        ),
        UnsyncActionScript(NPC_3),
        SetSyncActionScript(
            NPC_3, A0245_NIMBUS_5_EXIT_HALLWAY_FAKE_BIRD_STATUES_ACTIVATE
        ),
        JmpIfObjectInSpecificLevel(
            NPC_2,
            R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            ["EVENT_3704_fade_in_from_black_async_11"],
            identifier="EVENT_3704_jmp_if_object_in_level_7",
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_4,
            R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            ["EVENT_3704_fade_in_from_black_async_11"],
        ),
        UnsyncActionScript(NPC_4),
        SetSyncActionScript(
            NPC_4, A0245_NIMBUS_5_EXIT_HALLWAY_FAKE_BIRD_STATUES_ACTIVATE
        ),
        FadeInFromBlack(
            sync=False, identifier="EVENT_3704_fade_in_from_black_async_11"
        ),
        Return(),
    ]
)

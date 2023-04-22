# pylint: disable=C0301

"""E3712_NIMBUS_CASTLE_BRIDGE_ROOM_NPC_ANIMATIONS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_3, subscript=[ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)]
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_5,
            R111_NIMBUS_CASTLE_AREA_04_LEFT_OF_4WAY_PATH_RIGHTANGLE_RED_BRICK_PATH_W_TREASURE,
            ["EVENT_3712_jmp_if_object_not_in_level_6"],
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_4,
            R111_NIMBUS_CASTLE_AREA_04_LEFT_OF_4WAY_PATH_RIGHTANGLE_RED_BRICK_PATH_W_TREASURE,
            ["EVENT_3712_set_action_script_sync_10"],
        ),
        RunBackgroundEvent(
            event_id=E3711_NIMBUS_CASTLE_BRIDGE_ROOM_LOADER, return_on_level_exit=True
        ),
        FadeInFromBlack(sync=False),
        Return(),
        JmpIfObjectNotInSpecificLevel(
            NPC_4,
            R111_NIMBUS_CASTLE_AREA_04_LEFT_OF_4WAY_PATH_RIGHTANGLE_RED_BRICK_PATH_W_TREASURE,
            ["EVENT_3585_fade_in_from_black_async_0"],
            identifier="EVENT_3712_jmp_if_object_not_in_level_6",
        ),
        SetSyncActionScript(NPC_4, A0257_NIMBUS_PINWHEEL_LEFT),
        FadeInFromBlack(sync=False),
        Return(),
        SetSyncActionScript(
            NPC_5,
            A0881_NIMBUS_SHAMAN,
            identifier="EVENT_3712_set_action_script_sync_10",
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)

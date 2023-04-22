# pylint: disable=C0301

"""E3701_NIMBUS_CASTLE_LEFT_SHAMAN_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E0829_NIMBUS_CASTLE_EARLY_WEST_SHAMAN_PATH_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_3,
            R119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05,
            ["EVENT_3701_jmp_if_object_not_in_level_3"],
        ),
        FadeInFromBlack(sync=False),
        Return(),
        JmpIfObjectNotInSpecificLevel(
            NPC_2,
            R119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05,
            ["EVENT_3585_fade_in_from_black_async_0"],
            identifier="EVENT_3701_jmp_if_object_not_in_level_3",
        ),
        SetSyncActionScript(
            NPC_2,
            A0883_INC_PALETTE_ROW_FAKE_BIRD_STATUE,
            identifier="EVENT_3701_set_action_script_sync_4",
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)

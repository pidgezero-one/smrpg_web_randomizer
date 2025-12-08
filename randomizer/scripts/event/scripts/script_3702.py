# pylint: disable=C0301

"""E3702_NIMBUS_CASTLE_RIGHT_SHAMAN_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E0830_NIMBUS_CASTLE_EARLY_EAST_SHAMAN_PATH_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_3,
            R408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM_,
            ["EVENT_3702_jmp_if_object_not_in_level_3"]),
        FadeInFromBlack(sync=False),
        Return(),
        JmpIfObjectNotInSpecificLevel(
            NPC_2,
            R408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM_,
            ["EVENT_3585_fade_in_from_black_async_0"],
            identifier="EVENT_3702_jmp_if_object_not_in_level_3"),
        Jmp(["EVENT_3701_set_action_script_sync_4"]),
    ]
)

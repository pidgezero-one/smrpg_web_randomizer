# pylint: disable=C0301

"""E0391_MUSHROOM_KINGDOM_OCCUPIED_LEFT_STAIRWAY_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E0766_MUSHROOM_KINGDOM_OCCUPIED_STAIRWAY_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_1,
            R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM,
            ["EVENT_257_fade_in_from_black_async_0"],
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_4,
            R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
            ["EVENT_391_jmp_if_object_not_in_level_4"],
        ),
        FadeInFromBlack(sync=False),
        Return(),
        JmpIfObjectNotInSpecificLevel(
            NPC_2,
            R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM,
            ["EVENT_257_fade_in_from_black_async_0"],
            identifier="EVENT_391_jmp_if_object_not_in_level_4",
        ),
        ActionQueueAsync(
            target=NPC_2, subscript=[ASTransferToXYZF(x=25, y=28, z=0, direction=EAST)]
        ),
        JmpIfObjectInSpecificLevel(
            NPC_0,
            R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM,
            ["EVENT_391_fade_in_from_black_async_10"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_1,
            R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM,
            ["EVENT_391_fade_in_from_black_async_10"],
        ),
        FadeInFromBlack(sync=False),
        Return(),
        FadeInFromBlack(sync=False, identifier="EVENT_391_fade_in_from_black_async_10"),
        Return(),
    ]
)

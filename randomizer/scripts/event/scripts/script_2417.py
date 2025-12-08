# pylint: disable=C0301

"""E2417_TOWER_CHOMP_STAIRWAY_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_0,
            R040_BOOSTER_TOWER_8F_CHOMP_STAIRWAY,
            ["EVENT_2417_jmp_if_object_not_in_level_2"]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[ASSetWalkingSpeed(FASTEST), ASWalkSoutheastPixels(8)]),
        JmpIfObjectNotInSpecificLevel(
            NPC_1,
            R040_BOOSTER_TOWER_8F_CHOMP_STAIRWAY,
            ["EVENT_2417_jmp_if_object_not_in_level_4"],
            identifier="EVENT_2417_jmp_if_object_not_in_level_2"),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[ASSetWalkingSpeed(FASTEST), ASWalkSouthwestPixels(8)]),
        JmpIfObjectNotInSpecificLevel(
            NPC_2,
            R040_BOOSTER_TOWER_8F_CHOMP_STAIRWAY,
            ["EVENT_2417_fade_in_from_black_async_6"],
            identifier="EVENT_2417_jmp_if_object_not_in_level_4"),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[ASSetWalkingSpeed(FASTEST), ASWalkSoutheastPixels(8)]),
        FadeInFromBlack(sync=False, identifier="EVENT_2417_fade_in_from_black_async_6"),
        Return(),
    ]
)

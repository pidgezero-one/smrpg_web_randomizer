# pylint: disable=C0301

"""E1791_LANDS_END_UNDERGROUND_DOG_WALL_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(
            LANDS_END_UNDERGROUND_DOGS_TURNED_AROUND, ["EVENT_1791_jmp_to_event_4"]
        ),
        SetBit(LANDS_END_UNDERGROUND_DOGS_TURNED_AROUND),
        SetVarToConst(TIMER_701C, 90),
        RunBackgroundEventWithPauseReturnOnExit(
            event_id=E1788_LANDS_END_UNDERGROUND_DOG_WALL_ROOM_LOADER_BACKGROUND,
            timer_var=TIMER_701C),
        JmpToEvent(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_1791_jmp_to_event_4"),
    ]
)

# E1792_LANDS_END_UNDERGROUND_UPPER_PIT_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_0, subscript=[ASObjectMemorySetBit(arg_1=0x09, bits=[7])]
        ),
        ActionQueueSync(
            target=NPC_1, subscript=[ASObjectMemorySetBit(arg_1=0x09, bits=[7])]
        ),
        ActionQueueAsync(
            target=NPC_2, subscript=[ASObjectMemorySetBit(arg_1=0x09, bits=[7])]
        ),
        JmpIfBitSet(LANDS_END_UNDERGROUND_DOGS_MOVED, ["EVENT_1792_jmp_to_event_7"]),
        SetBit(LANDS_END_UNDERGROUND_DOGS_MOVED),
        SetVarToConst(TIMER_701C, 80),
        RunBackgroundEventWithPauseReturnOnExit(
            event_id=E1790_LANDS_END_UNDERGROUND_UPPER_PIT_ROOM_LOADER_BACKGROUND,
            timer_var=TIMER_701C,
        ),
        JmpToEvent(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_1792_jmp_to_event_7"),
    ]
)

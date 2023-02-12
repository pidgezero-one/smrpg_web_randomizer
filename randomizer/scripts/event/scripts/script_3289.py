# E3289_SHIP_COLLECT_TRAMPOLINE_PRIZE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(UNKNOWN_707D_1, ["EVENT_3289_ret_6"]),
        SetBit(UNKNOWN_707D_1),
        RunEventAsSubroutine(E0241_FREESTANDING_1_GRANT),
        Return(identifier="EVENT_3289_ret_6"),
    ]
)

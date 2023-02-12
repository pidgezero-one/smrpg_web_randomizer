# E3291_SHIP_COLLECT_CANNONBALL_PRIZE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(SHIP_CANNONBALL_PRIZE, ["EVENT_3289_ret_6"]),
        SetBit(SHIP_CANNONBALL_PRIZE),
        RunEventAsSubroutine(E0241_FREESTANDING_1_GRANT),
        Return(),
    ]
)

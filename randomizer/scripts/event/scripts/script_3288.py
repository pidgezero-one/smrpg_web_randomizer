# E3288_SHIP_SPAWN_PRIZE_IN_TROOPA_PUZZLE_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(SHIP_TROOPA_PRIZE, ["EVENT_3288_ret_8"]),
        SetBit(SHIP_TROOPA_PRIZE),
        RunEventAsSubroutine(E0241_FREESTANDING_1_GRANT),
        Return(identifier="EVENT_3288_ret_8"),
    ]
)

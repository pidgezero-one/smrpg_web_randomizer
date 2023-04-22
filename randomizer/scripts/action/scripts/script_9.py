"""A0009_SEWER_BOSS_ROOM_TRAMPOLINE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        JmpIfBitClear(SEWER_BOSS_DEFEATED, ["ACTION_9_visibility_on_4"]),
        VisibilityOff(),
        ClearSolidityBits(
            bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
        ),
        Return(),
        VisibilityOn(identifier="ACTION_9_visibility_on_4"),
        SequenceLoopingOff(),
        Return(),
    ]
)

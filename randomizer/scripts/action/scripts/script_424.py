"""A0424_GOOMBA_THUMPIN_SPINY"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        JmpToSubroutine(["ACTION_424_clear_solidity_bits_2"]),
        Jmp(["ACTION_416_transfer_to_xyzf_47"]),
        ClearSolidityBits(
            bit_4=True,
            cant_pass_npcs=True,
            cant_walk_through=True,
            bit_7=True,
            identifier="ACTION_424_clear_solidity_bits_2"),
        ShiftZDownPixels(2),
        VisibilityOff(),
        Return(),
    ]
)

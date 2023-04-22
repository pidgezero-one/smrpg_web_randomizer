"""A0426_GOOMBA_THUMPIN_SPINY"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        JmpToSubroutine(["ACTION_424_clear_solidity_bits_2"]),
        Jmp(["ACTION_418_transfer_to_xyzf_47"]),
    ]
)

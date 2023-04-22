"""A0423_GOOMBA_THUMPIN_BONK"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        JmpToSubroutine(["ACTION_420_set_sprite_sequence_2"]),
        Jmp(["ACTION_419_transfer_to_xyzf_47"]),
    ]
)

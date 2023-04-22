"""A0421_GOOMBA_THUMPIN_BONK"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        JmpToSubroutine(["ACTION_420_set_sprite_sequence_2"]),
        Jmp(["ACTION_417_transfer_to_xyzf_47"]),
    ]
)

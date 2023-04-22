"""A0905_COIN_SHOWER_E_DB"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F, pixel=True),
        FaceEast7C(),
        Jmp(["ACTION_903_jump_to_height_silent_1"]),
    ]
)

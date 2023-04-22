"""A0117_PIPE_VAULT_CHOMPWEED_PLATFORM"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FixedFCoordOn(identifier="ACTION_117_fixed_f_coord_on_0"),
        WalkNortheastSteps(3),
        WalkSouthwestSteps(3),
        Jmp(["ACTION_117_fixed_f_coord_on_0"]),
    ]
)

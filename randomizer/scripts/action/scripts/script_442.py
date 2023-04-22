"""A0442_ROSE_WAY_CROOK"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Pause(25, identifier="ACTION_442_pause_0"),
        FaceMario(),
        JmpIfObjectWithinRange(
            comparing_npc=MARIO,
            usually=0,
            tiles=5,
            destinations=["ACTION_442_set_animation_speed_4"],
        ),
        Jmp(["ACTION_442_pause_0"]),
        SetWalkingSpeed(FAST, identifier="ACTION_442_set_animation_speed_4"),
        SequencePlaybackOn(),
        SetSolidityBits(cant_pass_walls=True),
        WalkFDirectionSteps(2),
        FaceMario(),
        WalkFDirectionSteps(2),
        FaceMario(),
        WalkFDirectionSteps(2),
        SequencePlaybackOff(),
        Jmp(["ACTION_442_pause_0"]),
    ]
)

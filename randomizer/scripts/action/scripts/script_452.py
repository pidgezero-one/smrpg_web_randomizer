"""A0452_FACTORY_FOUR_SCREW_ROOM_AMEBOID"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSpriteSequence(
            index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        JmpIfBitClear(DIRECTIONAL_7045_7, ["ACTION_452_pause_3"]),
        Pause(176),
        Pause(1, identifier="ACTION_452_pause_3"),
        JmpIfObjectWithinRangeSameZ(
            comparing_npc=MARIO,
            usually=0,
            tiles=2,
            destinations=["ACTION_452_sequence_looping_on_6"],
        ),
        Jmp(["ACTION_452_pause_3"]),
        SequenceLoopingOn(identifier="ACTION_452_sequence_looping_on_6"),
        SetSpriteSequence(index=8, looping=False, mirror_sprite=True),
        Pause(48),
        WalkNorthwestSteps(2, identifier="ACTION_452_shift_northwest_steps_9"),
        Pause(8),
        FaceNortheast(),
        Pause(8),
        WalkSoutheastSteps(2),
        Pause(8),
        FaceSouthwest(),
        Pause(8),
        Jmp(["ACTION_452_shift_northwest_steps_9"]),
    ]
)

"""A0308_SHIP_FIRST_WHIRLPOOL_ROOM_FISH"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetMovementsBits(bit_0=True, cant_walk_under=True),
        SetWalkingSpeed(SLOW),
        SequenceLoopingOn(),
        Db(bytearray(b" \x04")),
        EmbeddedAnimationRoutine(
            bytearray(b"(\x00\x00\x00\x00\x00\x00\x00\x10\x00\x01\x00\x00\x80\x00\x80")
        ),
        TurnRandomDirection(identifier="ACTION_308_turn_random_direction_5"),
        WalkFDirectionSteps(2),
        FaceMario(),
        Walk1StepFDirection(),
        TurnRandomDirection(),
        WalkFDirectionSteps(2),
        JmpIfObjectWithinRangeSameZ(
            comparing_npc=MARIO,
            usually=0,
            tiles=4,
            destinations=["ACTION_308_face_mario_13"],
        ),
        Jmp(["ACTION_308_turn_random_direction_5"]),
        FaceMario(identifier="ACTION_308_face_mario_13"),
        SetWalkingSpeed(NORMAL),
        SetSequenceSpeed(FAST),
        Walk1StepFDirection(),
        SetWalkingSpeed(SLOW),
        SetSequenceSpeed(NORMAL),
        Jmp(["ACTION_308_turn_random_direction_5"]),
    ]
)

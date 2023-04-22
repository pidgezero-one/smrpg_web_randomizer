"""A0549_KEEP_CROSSING_TERRA_COTTAS_BASE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Dec(GAME_OVER_COUNTER_MAYBE, identifier="ACTION_549_dec_0"),
        ResetProperties(),
        SetWalkingSpeed(NORMAL),
        SetSequenceSpeed(FAST),
        Pause(16),
        SetSolidityBits(
            cant_pass_walls=True, identifier="ACTION_549_set_solidity_bits_5"
        ),
        JmpIfRandom2of3(["ACTION_549_face_mario_10", "ACTION_549_face_mario_10"]),
        TurnRandomDirection(),
        Walk1StepFDirection(),
        Jmp(["ACTION_549_set_solidity_bits_5"]),
        FaceMario(identifier="ACTION_549_face_mario_10"),
        Walk1StepFDirection(),
        Jmp(["ACTION_549_set_solidity_bits_5"]),
    ]
)

"""A0998_KEEP_ORIGINAL_THRONE_ROOM_GOOMBA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FaceSoutheast(),
        SetSequenceSpeed(NORMAL),
        SequenceLoopingOn(),
        Pause(1, identifier="ACTION_998_pause_3"),
        JmpIfBitSet(TEMP_7043_0, ["ACTION_998_clear_solidity_bits_6"]),
        Jmp(["ACTION_998_pause_3"]),
        ClearSolidityBits(
            cant_pass_walls=True, identifier="ACTION_998_clear_solidity_bits_6"
        ),
        SequenceLoopingOn(),
        SetSequenceSpeed(VERY_FAST),
        SetWalkingSpeed(FAST),
        JumpToHeight(height=96, silent=True),
        WalkSoutheastSteps(2),
        SequenceLoopingOff(),
        Pause(30),
        Jmp(["ACTION_997_sequence_playback_on_0"]),
    ]
)

"""A0729_EXPLODING_MICROBOMB"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        VisibilityOff(identifier="ACTION_729_visibility_off_0"),
        Pause(1),
        JmpIfBitClear(TEMP_7043_4, ["ACTION_729_visibility_off_0"]),
        VisibilityOn(),
        SequenceLoopingOn(),
        PlaySound(sound=SO089_LIT_FUSE, channel=4),
        SequencePlaybackOn(),
        SetSpriteSequence(index=2, is_sequence=True, looping=True),
        Pause(60),
        SetSpriteSequence(index=3, is_sequence=True, looping=False),
        Pause(20),
        VisibilityOff(),
        Db(bytearray(b"\xc7\x07")),
        StartLoopNTimes(2),
        AddConstToVar(Z_COORD_1, 32),
        JmpToSubroutine(["ACTION_729_pause_42"]),
        CreatePacketAt7010(
            packet=P024_REGULAR_SOUND_EXPLOSION, destinations=["ACTION_729_pause_38"]
        ),
        AddConstToVar(Z_COORD_1, 32),
        AddConstToVar(X_COORD_1, 64),
        Pause(10),
        JmpToSubroutine(["ACTION_729_pause_42"]),
        CreatePacketAt7010(
            packet=P024_REGULAR_SOUND_EXPLOSION, destinations=["ACTION_729_pause_38"]
        ),
        AddConstToVar(Z_COORD_1, 32),
        AddConstToVar(X_COORD_1, 65408),
        Pause(11),
        JmpToSubroutine(["ACTION_729_pause_42"]),
        CreatePacketAt7010(
            packet=P024_REGULAR_SOUND_EXPLOSION, destinations=["ACTION_729_pause_38"]
        ),
        AddConstToVar(Z_COORD_1, 32),
        AddConstToVar(Y_COORD_1, 64),
        Pause(9),
        JmpToSubroutine(["ACTION_729_pause_42"]),
        CreatePacketAt7010(
            packet=P024_REGULAR_SOUND_EXPLOSION, destinations=["ACTION_729_pause_38"]
        ),
        AddConstToVar(Z_COORD_1, 32),
        AddConstToVar(Y_COORD_1, 65472),
        AddConstToVar(X_COORD_1, 64),
        Pause(11),
        JmpToSubroutine(["ACTION_729_pause_42"]),
        CreatePacketAt7010(
            packet=P024_REGULAR_SOUND_EXPLOSION, destinations=["ACTION_729_pause_38"]
        ),
        Pause(10, identifier="ACTION_729_pause_38"),
        EndLoop(),
        SetBit(TEMP_7043_5),
        Return(),
        Pause(1, identifier="ACTION_729_pause_42"),
        JmpIfBitSet(BAMBINO_BOMB_UNKNOWN, ["ACTION_729_pause_42"]),
        Return(),
    ]
)

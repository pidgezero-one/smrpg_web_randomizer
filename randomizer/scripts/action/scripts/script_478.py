"""A0478_BANDITS_WAY_1ST_PLATFORMS_SWING"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetPriority(2),
        VisibilityOff(),
        TransferToObjectXY(MEM_70A9),
        VisibilityOn(),
        Db(bytearray(b" \x03")),
        EmbeddedAnimationRoutine(
            bytearray(b"&\x00\x00\x00\x00\x00\x00\x000\x00\x01\x00\x00\x00\x04\x80")
        ),
        EmbeddedAnimationRoutine(
            bytearray(b"'\x00\x00\x00\x00\x00\xc0\x00 \x00\x01\x00\x00\x00\x04\x80")
        ),
        CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_700C),
        Db(bytearray(b"\xfd%")),
        Pause(1, identifier="ACTION_478_pause_9"),
        Jmp(["ACTION_478_pause_9"]),
    ]
)

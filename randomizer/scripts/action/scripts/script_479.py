"""A0479_BANDITS_WAY_CHEST_PLATFORMS_ON_MOUNT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        VisibilityOff(),
        TransferToObjectXY(MEM_70A9),
        VisibilityOn(),
        Db(bytearray(b" \x03")),
        EmbeddedAnimationRoutine(
            bytearray(b"&\x00\x00\x00\x00\x00\x00\x00,\x00\x01\x00\x00\x80\x00\x80")
        ),
        EmbeddedAnimationRoutine(
            bytearray(b"'\x00\x00\x00\x00\x00\xc0\x00 \x00\x01\x00\x00\x80\x00\x80")
        ),
        CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_700C),
        Db(bytearray(b"\xfd%")),
        Pause(1, identifier="ACTION_479_pause_8"),
        Jmp(["ACTION_479_pause_8"]),
    ]
)

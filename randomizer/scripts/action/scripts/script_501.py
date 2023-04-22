"""A0501_MUSHROOM_DERBY_UNKNOWN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        BPL262728(),
        SetSequenceSpeed(VERY_FAST),
        Db(bytearray(b" \x03")),
        Db(bytearray(b"$@\x01`\xff")),
        Pause(14),
        SetBit(TEMP_7043_2),
        Jmp(["ACTION_500_db_0"]),
    ]
)

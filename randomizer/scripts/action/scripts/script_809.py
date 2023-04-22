"""A0809_MARIO_BLOWN_BY_FAN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Set700CToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 117, ["ACTION_809_db_6"]),
        Db(bytearray(b" \x03")),
        Db(bytearray(b"$\x00\xfe\x00\x01")),
        Pause(1, identifier="ACTION_809_pause_4"),
        Jmp(["ACTION_809_pause_4"]),
        Db(bytearray(b" \x03"), identifier="ACTION_809_db_6"),
        Db(bytearray(b"$\x00\x02\x00\x01")),
        Jmp(["ACTION_809_pause_4"]),
    ]
)

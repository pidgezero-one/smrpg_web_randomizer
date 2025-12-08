# pylint: disable=C0301,C0103

"""referenced by monster_spells Flame, monster_attacks Blazer"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=27,
    script=[
        RunSubroutine(["command_0x35259b"], identifier="queuestart_0x356b4b"),
        Db(bytearray(b"\x83\x83")),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
        Jmp(["command_0x356af4"]),
        RunSubroutine(["command_0x35259b"], identifier="queuestart_0x356b57"),
        Db(bytearray(b"\x83\x83")),
        RunSubroutine(["command_0x352c01"]),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=20),
        Jmp(["command_0x356af4"]),
    ])

# pylint: disable=C0301,C0103

"""referenced by """

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=102,
    script=[
        Db(bytearray(b"b")),
        PauseScriptUntil(condition=0x68),
        PauseScriptUntil(condition=0x88),
        PauseScriptUntil(condition=0xCE),
        PauseScriptUntil(condition=0x02),
        PauseScriptUntil(condition=0x68),
        PauseScriptUntil(condition=0x8F),
        PauseScriptUntil(condition=0xD5),
        PauseScriptUntil(condition=0x02),
        PauseScriptUntil(condition=0x68),
        PauseScriptUntil(condition=0x96),
        PauseScriptUntil(condition=0xDC),
        PauseScriptUntil(condition=0x02),
        PauseScriptUntil(condition=0x68),
        PauseScriptUntil(condition=0x9D),
        PauseScriptUntil(condition=0xE3),
        PauseScriptUntil(condition=0x02),
        PauseScriptUntil(condition=0x68),
        PauseScriptUntil(condition=0xA4),
        PauseScriptUntil(condition=0xEA),
        PauseScriptUntil(condition=0x02),
        PauseScriptUntil(condition=0x68),
        PauseScriptUntil(condition=0x88),
        PauseScriptUntil(condition=0xCE),
        PauseScriptUntil(condition=0x02),
        Db(bytearray(b"\x14"), identifier="command_0x350463"),
        Pause1Frame(),
        Jmp(["command_0x350463"]),
    ])

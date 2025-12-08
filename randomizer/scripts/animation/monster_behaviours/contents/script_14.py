"""behaviour_14_0x350916 animation"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=6,
    script=[
        VisibilityOff(identifier="command_0x350916"),
        Db(bytearray(b"O")),
        Jmp(["command_0x3508a9"]),
    ])

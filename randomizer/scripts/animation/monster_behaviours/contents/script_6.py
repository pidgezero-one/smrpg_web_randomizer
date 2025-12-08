"""behaviour_6_0x350790 animation"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=6,
    script=[
        VisibilityOff(identifier="command_0x350790"),
        Db(bytearray(b"O")),
        Jmp(["command_0x3505c9"]),
    ])

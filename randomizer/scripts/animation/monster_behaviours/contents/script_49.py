"""behaviour_49_0x350F44 animation"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=6,
    script=[
        VisibilityOff(identifier="command_0x350f44"),
        Db(bytearray(b"O")),
        Jmp(["command_0x350e87"]),
    ],
)

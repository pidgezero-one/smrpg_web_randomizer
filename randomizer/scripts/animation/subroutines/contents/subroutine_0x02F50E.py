# pylint: disable=C0301,C0103

"""referenced by toad_tutorial"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=16,
    script=[
        SpriteSequence(
            sequence=1, looping_off=True, mirror=True, identifier="command_0x2f50e"
        ),
        Jmp(["command_0x2f4f5"]),
        Set7E1xToAMEM8Bit(0x7EE000, 0x6A, identifier="command_0x2f513"),
        Db(bytearray(b"G\x08\x1e\xf5")),
        Jmp(["command_0x2f4f5"]),
    ])

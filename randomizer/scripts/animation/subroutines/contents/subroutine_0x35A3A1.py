# pylint: disable=C0301,C0103

"""referenced by ally_spells Sleepy Time"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=23,
    script=[
        SetAMEM32ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=207,
            y=-16,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x35a3a1",
        ),
        Db(bytearray(b"\x83\x83")),
        SetAMEM40ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=207,
            y=163,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        RunSubroutine(["command_0x35a45b"]),
        RemoveObject(),
        ReturnObjectQueue(),
    ],
)

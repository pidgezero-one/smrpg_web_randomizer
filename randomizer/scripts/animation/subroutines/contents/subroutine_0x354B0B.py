# pylint: disable=C0301,C0103

"""referenced by monster_attacks PhysicalAttack51"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=38,
    script=[
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=0,
            y=0,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x354b0b",
        ),
        DoMaskEffect(POLYGON_MASK),
        RunSubroutine(["command_0x35336f"]),
        RunSubroutine(["command_0x3533ea"]),
        SetMaskCoords((8, -88), (16, -56), (68, 8), (-8, 8)),
        RunSubroutine(["command_0x3533f5"]),
        RunSubroutine(["command_0x3533a7"]),
        RunSubroutine(["command_0x353416"]),
        Db(bytearray(b"\xc4")),
        Db(bytearray(b"\xc5")),
        ReturnObjectQueue(),
    ],
)

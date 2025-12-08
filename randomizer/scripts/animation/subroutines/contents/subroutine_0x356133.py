# pylint: disable=C0301,C0103

"""referenced by monster_attacks PhysicalAttack40"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=31,
    script=[
        SetAMEM60ToCurrentTarget(identifier="queuestart_0x356133"),
        SetAMEM32ToXYZCoords(
            origin=TARGET_CURRENT_POSITION,
            x=3,
            y=-16,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        Db(bytearray(b" \xbeC\x00")),
        JmpIfAMEM8BitNotEqualsConst(0x6E, 4, ["command_0x35253b"]),
        SetAMEM16BitToConst(0x60, 20),
        RunSubroutine(["command_0x35249d"]),
        PlaySound(sound=S0115_TRANSFORM),
        RunSubroutine(["command_0x35253b"]),
    ])

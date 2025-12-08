"""BE0060_BELOME_CLONES_SOMEONE"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    script=[
        RunSubroutine(["command_0x3a7531"]),
        SpriteQueue(
            field_object=0, destinations=["queuestart_0x3ad9bc"], bit_2=True, bit_4=True
        ),
        RunSubroutine(["command_0x3a7729"]),
        SetAMEM8BitTo7E1x(0x60, 0x7EE00E),
        JmpIfAMEMBitsSet(0x60, [0], ["command_0x3a68b1"]),
        SpriteQueue(
            field_object=1, destinations=["queuestart_0x3ad9d2"], bit_2=True, bit_4=True
        ),
        Jmp(["command_0x3a68b6"]),
        SpriteQueue(
            field_object=2,
            destinations=["queuestart_0x3ada5c"],
            bit_2=True,
            bit_4=True,
            identifier="command_0x3a68b1"),
        RunSubroutine(["command_0x3a771e"], identifier="command_0x3a68b6"),
        Jmp(["command_0x3a7550"]),
    ]
)

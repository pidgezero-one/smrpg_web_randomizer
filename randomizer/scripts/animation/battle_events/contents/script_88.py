"""BE0088_SMITHY_TRANSFORMS_INTO_MAGIC_HEAD"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    script=[
        RunSubroutine(["command_0x3a7531"]),
        SpriteQueue(
            field_object=2, destinations=["queuestart_0x3ae2cd"], bit_2=True, bit_4=True
        ),
        SetAMEM8BitTo7E1x(0x60, 0x7EE009),
        JmpIfAMEM8BitEqualsConst(0x60, 1, ["command_0x3a6e1c"]),
        JmpIfAMEM8BitEqualsConst(0x60, 2, ["command_0x3a6e24"]),
        JmpIfAMEM8BitEqualsConst(0x60, 3, ["command_0x3a6e2c"]),
        JmpIfAMEM8BitEqualsConst(0x60, 4, ["command_0x3a6e34"]),
        ClearAMEM8Bit(0x60),
        Set7E1xToAMEM8Bit(0x7EE009, 0x60),
        SpriteQueue(
            field_object=1,
            destinations=["queuestart_0x3ae254"],
            bit_2=True,
            bit_4=True,
            identifier="command_0x3a6e1c"),
        Jmp(["command_0x3a6e3f"]),
        SpriteQueue(
            field_object=1,
            destinations=["queuestart_0x3ae231"],
            bit_2=True,
            bit_4=True,
            identifier="command_0x3a6e24"),
        Jmp(["command_0x3a6e3f"]),
        SpriteQueue(
            field_object=1,
            destinations=["queuestart_0x3ae231"],
            bit_2=True,
            bit_4=True,
            identifier="command_0x3a6e2c"),
        Jmp(["command_0x3a6e3f"]),
        SpriteQueue(
            field_object=1,
            destinations=["queuestart_0x3ae277"],
            bit_2=True,
            bit_4=True,
            identifier="command_0x3a6e34"),
        ClearAMEM8Bit(0x60),
        Set7E1xToAMEM8Bit(0x7EE009, 0x60),
        RunSubroutine(["command_0x3a771e"], identifier="command_0x3a6e3f"),
        Jmp(["command_0x3a7550"]),
    ]
)

"""BE0094_PUNCHINELLO_S_BOMBS_EXPLODE_IF_STILL_ALIVE"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    script=[
        RunSubroutine(["command_0x3a7531"]),
        ClearAMEM8Bit(0x60),
        SpriteQueue(
            field_object=1, destinations=["queuestart_0x3aba9e"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=2, destinations=["queuestart_0x3aba9e"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=3, destinations=["queuestart_0x3aba9e"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=4, destinations=["queuestart_0x3aba9e"], bit_2=True, bit_4=True
        ),
        Pause1Frame(identifier="command_0x3a6f42"),
        JmpIfAMEM8BitNotEqualsConst(0x60, 4, ["command_0x3a6f42"]),
        Jmp(["command_0x3a7550"]),
    ]
)

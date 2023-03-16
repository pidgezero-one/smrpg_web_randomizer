"""BE0009_PUNCHINELLO_INTERLUDES_AND_PREPARES_TO_SUMMON_BOB_OMBS"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    script=[
        RunSubroutine(["command_0x3a7531"]),
        SpriteQueue(
            field_object=0, destinations=["queuestart_0x3ababb"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=1, destinations=["queuestart_0x3ab9a0"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=2, destinations=["queuestart_0x3ab9ba"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=3, destinations=["queuestart_0x3ab9d4"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=4, destinations=["queuestart_0x3ab9ee"], bit_2=True, bit_4=True
        ),
        RunSubroutine(["command_0x3a771e"]),
        Jmp(["command_0x3a7550"]),
    ]
)

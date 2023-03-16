"""BE0074_CULEX_SUMMONS_CRYSTALS"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    script=[
        RunSubroutine(["command_0x3a7531"]),
        SpriteQueue(
            field_object=1, destinations=["queuestart_0x3ade84"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=2, destinations=["queuestart_0x3ade9e"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=3, destinations=["queuestart_0x3adeb8"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=4, destinations=["queuestart_0x3aded2"], bit_2=True, bit_4=True
        ),
        Jmp(["command_0x3a7550"]),
    ]
)

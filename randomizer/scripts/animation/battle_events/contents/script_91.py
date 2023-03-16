"""BE0091_SMITHY_S_HEAD_FADES_BEFORE_TRANSFORMING_INTO_OTHER_HEAD"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    script=[
        RunSubroutine(["command_0x3a7531"]),
        SpriteQueue(
            field_object=2, destinations=["queuestart_0x3acf48"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=1, destinations=["queuestart_0x3ae29a"], bit_2=True, bit_4=True
        ),
        RunSubroutine(["command_0x3a771e"]),
        Jmp(["command_0x3a7550"]),
    ]
)

"""BE0046_CZAR_DRAGON_SUMMONS_HELIOS"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    script=[
        RunSubroutine(["command_0x3a7531"]),
        SpriteQueue(
            field_object=0, destinations=["queuestart_0x3acf1a"], bit_2=True, bit_4=True
        ),
        RunSubroutine(["command_0x3a7729"]),
        SpriteQueue(
            field_object=2, destinations=["queuestart_0x3ace4f"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=3, destinations=["queuestart_0x3ace81"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=4, destinations=["queuestart_0x3aceb3"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=5, destinations=["queuestart_0x3acee5"], bit_2=True, bit_4=True
        ),
        RunSubroutine(["command_0x3a7734"]),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=60),
        RunSubroutine(["command_0x3a755e"]),
        Jmp(["command_0x3a7550"]),
    ]
)

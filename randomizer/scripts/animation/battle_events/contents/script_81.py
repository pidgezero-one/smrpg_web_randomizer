"""BE0081_EXOR_IS_DEFEATED_CRIES_AND_OPENS_MOUTH"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    script=[
        RunSubroutine(["command_0x3a7531"]),
        SpriteQueue(
            field_object=0, destinations=["queuestart_0x3ae0cc"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=1, destinations=["queuestart_0x3ae0d9"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=2, destinations=["queuestart_0x3ae0e8"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=3, destinations=["queuestart_0x3ae0f8"], bit_2=True, bit_4=True
        ),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=200),
        Jmp(["command_0x3a7550"]),
    ]
)

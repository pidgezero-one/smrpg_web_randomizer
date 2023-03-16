"""BE0047_UNKNOWN"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    script=[
        RunSubroutine(["command_0x3a7531"]),
        SpriteQueue(
            field_object=1, destinations=["queuestart_0x3ad15a"], bit_2=True, bit_4=True
        ),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=200),
        RunSubroutine(["command_0x3a771e"]),
        Jmp(["command_0x3a7550"]),
    ]
)

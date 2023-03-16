"""BE0019_KNIFE_GUY_GRATE_GUY_SEPARATE_YIKES_THEY_RE_PRETTY_TOUGH"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    script=[
        RunSubroutine(["command_0x3a7531"]),
        SpriteQueue(
            field_object=0, destinations=["queuestart_0x3abf91"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=1, destinations=["queuestart_0x3abfca"], bit_2=True, bit_4=True
        ),
        RunSubroutine(["command_0x3a771e"]),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=60),
        Jmp(["command_0x3a7550"]),
    ]
)

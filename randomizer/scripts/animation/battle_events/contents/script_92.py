"""BE0092_SHELLY_BREAKS"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    script=[
        RunSubroutine(["command_0x3a7531"]),
        SetAMEM16BitToConst(0x60, 0),
        ObjectQueueAtOffsetAndIndex(
            index=8, target_address=0x3A8AC0, identifier="set_shelly_fragment"
        ),
        RunSubroutine(["command_0x3a771e"]),
        Jmp(["command_0x3a7550"]),
    ]
)

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35C71F,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35C71F import (
    script as subroutine_0x35C71F,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35C71F,
    start=0x35C71F,
    end=0x35C760,
    scripts=[
        subroutine_0x35C71F,
    ],
)

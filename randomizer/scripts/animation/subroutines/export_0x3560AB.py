from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3560AB,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3560AB import (
    script as subroutine_0x3560AB,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3560AB,
    start=0x3560AB,
    end=0x3560CC,
    scripts=[
        subroutine_0x3560AB,
    ],
)

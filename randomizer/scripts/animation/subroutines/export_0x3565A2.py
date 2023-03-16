from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3565A2,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3565A2 import (
    script as subroutine_0x3565A2,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3565A2,
    start=0x3565A2,
    end=0x3565FE,
    scripts=[
        subroutine_0x3565A2,
    ],
)

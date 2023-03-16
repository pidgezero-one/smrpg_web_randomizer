from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X356525,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x356525 import (
    script as subroutine_0x356525,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356525,
    start=0x356525,
    end=0x35659F,
    scripts=[
        subroutine_0x356525,
    ],
)

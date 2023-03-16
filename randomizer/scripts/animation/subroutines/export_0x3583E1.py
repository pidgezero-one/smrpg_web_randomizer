from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3583E1,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3583E1 import (
    script as subroutine_0x3583E1,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3583E1,
    start=0x3583E1,
    end=0x358439,
    scripts=[
        subroutine_0x3583E1,
    ],
)

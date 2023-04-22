# pylint: disable=C0301,C0103

"""exports subroutine 0X352F25"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X352F25,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x352F25 import (
    script as subroutine_0x352F25,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X352F25,
    start=0x352F25,
    end=0x3530F2,
    scripts=[
        subroutine_0x352F25,
    ],
)

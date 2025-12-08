# pylint: disable=C0301,C0103

"""exports subroutine 0X352D5F"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X352D5F)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x352D5F import (
    script as subroutine_0x352D5F)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X352D5F,
    start=0x352D5F,
    end=0x352D67,
    scripts=[
        subroutine_0x352D5F,
    ])

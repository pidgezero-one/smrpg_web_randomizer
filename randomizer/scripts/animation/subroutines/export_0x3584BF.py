# pylint: disable=C0301,C0103

"""exports subroutine 0X3584BF"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3584BF)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3584BF import (
    script as subroutine_0x3584BF)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3584BF,
    start=0x3584BF,
    end=0x358684,
    scripts=[
        subroutine_0x3584BF,
    ])

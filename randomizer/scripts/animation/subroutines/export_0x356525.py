# pylint: disable=C0301,C0103

"""exports subroutine 0X356525"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X356525)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x356525 import (
    script as subroutine_0x356525)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356525,
    start=0x356525,
    end=0x35659F,
    scripts=[
        subroutine_0x356525,
    ])

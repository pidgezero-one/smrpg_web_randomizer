# pylint: disable=C0301,C0103

"""exports subroutine 0X3A80AC"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3A80AC)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A80AC import (
    script as subroutine_0x3A80AC)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A80AC,
    start=0x3A80AC,
    end=0x3A80B5,
    scripts=[
        subroutine_0x3A80AC,
    ])

# pylint: disable=C0301,C0103

"""exports subroutine 0X3ACF48"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3ACF48)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3ACF48 import (
    script as subroutine_0x3ACF48)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3ACF48,
    start=0x3ACF48,
    end=0x3AD6F3,
    scripts=[
        subroutine_0x3ACF48,
    ])

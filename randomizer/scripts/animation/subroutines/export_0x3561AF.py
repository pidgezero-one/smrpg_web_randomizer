# pylint: disable=C0301,C0103

"""exports subroutine 0X3561AF"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3561AF)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3561AF import (
    script as subroutine_0x3561AF)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3561AF,
    start=0x3561AF,
    end=0x3561DF,
    scripts=[
        subroutine_0x3561AF,
    ])

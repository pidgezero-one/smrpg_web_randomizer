# pylint: disable=C0301,C0103

"""exports subroutine 0X357348"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X357348)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x357348 import (
    script as subroutine_0x357348)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X357348,
    start=0x357348,
    end=0x357399,
    scripts=[
        subroutine_0x357348,
    ])

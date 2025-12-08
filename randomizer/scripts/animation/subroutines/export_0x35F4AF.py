# pylint: disable=C0301,C0103

"""exports subroutine 0X35F4AF"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35F4AF)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35F4AF import (
    script as subroutine_0x35F4AF)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F4AF,
    start=0x35F4AF,
    end=0x35F541,
    scripts=[
        subroutine_0x35F4AF,
    ])

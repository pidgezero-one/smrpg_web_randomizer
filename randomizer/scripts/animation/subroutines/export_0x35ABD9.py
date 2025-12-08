# pylint: disable=C0301,C0103

"""exports subroutine 0X35ABD9"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35ABD9)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35ABD9 import (
    script as subroutine_0x35ABD9)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35ABD9,
    start=0x35ABD9,
    end=0x35ABF5,
    scripts=[
        subroutine_0x35ABD9,
    ])

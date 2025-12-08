# pylint: disable=C0301,C0103

"""exports subroutine 0X35BEB8"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35BEB8)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35BEB8 import (
    script as subroutine_0x35BEB8)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35BEB8,
    start=0x35BEB8,
    end=0x35BF61,
    scripts=[
        subroutine_0x35BEB8,
    ])

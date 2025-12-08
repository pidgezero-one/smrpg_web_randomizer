# pylint: disable=C0301,C0103

"""exports subroutine 0X35691B"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35691B)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35691B import (
    script as subroutine_0x35691B)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35691B,
    start=0x35691B,
    end=0x356968,
    scripts=[
        subroutine_0x35691B,
    ])

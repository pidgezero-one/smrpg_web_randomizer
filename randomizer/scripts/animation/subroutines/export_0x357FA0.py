# pylint: disable=C0301,C0103

"""exports subroutine 0X357FA0"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X357FA0)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x357FA0 import (
    script as subroutine_0x357FA0)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X357FA0,
    start=0x357FA0,
    end=0x357FE1,
    scripts=[
        subroutine_0x357FA0,
    ])

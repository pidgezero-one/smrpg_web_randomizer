# pylint: disable=C0301,C0103

"""exports subroutine 0X356089"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X356089)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x356089 import (
    script as subroutine_0x356089)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356089,
    start=0x356089,
    end=0x3560A8,
    scripts=[
        subroutine_0x356089,
    ])

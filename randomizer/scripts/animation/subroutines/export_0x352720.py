# pylint: disable=C0301,C0103

"""exports subroutine 0X352720"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X352720)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x352720 import (
    script as subroutine_0x352720)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X352720,
    start=0x352720,
    end=0x352731,
    scripts=[
        subroutine_0x352720,
    ])

# pylint: disable=C0301,C0103

"""exports subroutine 0X352DC0"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X352DC0)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x352DC0 import (
    script as subroutine_0x352DC0)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X352DC0,
    start=0x352DC0,
    end=0x352DC7,
    scripts=[
        subroutine_0x352DC0,
    ])

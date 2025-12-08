# pylint: disable=C0301,C0103

"""exports subroutine 0X354306"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X354306)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x354306 import (
    script as subroutine_0x354306)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X354306,
    start=0x354306,
    end=0x3543B8,
    scripts=[
        subroutine_0x354306,
    ])

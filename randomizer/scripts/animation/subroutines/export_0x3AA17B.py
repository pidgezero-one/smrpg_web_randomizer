# pylint: disable=C0301,C0103

"""exports subroutine 0X3AA17B"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3AA17B)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3AA17B import (
    script as subroutine_0x3AA17B)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3AA17B,
    start=0x3AA17B,
    end=0x3AA242,
    scripts=[
        subroutine_0x3AA17B,
    ])

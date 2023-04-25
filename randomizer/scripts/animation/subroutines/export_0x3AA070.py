# pylint: disable=C0301,C0103

"""exports subroutine 0X3AA070"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3AA070,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3AA070 import (
    script as subroutine_0x3AA070,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3AA070,
    start=0x3AA070,
    end=0x3AA140,
    scripts=[
        subroutine_0x3AA070,
    ],
)

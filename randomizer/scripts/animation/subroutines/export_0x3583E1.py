# pylint: disable=C0301,C0103

"""exports subroutine 0X3583E1"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3583E1,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3583E1 import (
    script as subroutine_0x3583E1,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3583E1,
    start=0x3583E1,
    end=0x358439,
    scripts=[
        subroutine_0x3583E1,
    ],
)

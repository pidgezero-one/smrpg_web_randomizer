# pylint: disable=C0301,C0103

"""exports subroutine 0X3531F8"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3531F8,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3531F8 import (
    script as subroutine_0x3531F8,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3531F8,
    start=0x3531F8,
    end=0x3532D0,
    scripts=[
        subroutine_0x3531F8,
    ],
)

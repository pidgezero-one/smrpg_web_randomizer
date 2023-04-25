# pylint: disable=C0301,C0103

"""exports subroutine 0X3573AC"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3573AC,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3573AC import (
    script as subroutine_0x3573AC,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3573AC,
    start=0x3573AC,
    end=0x3575FB,
    scripts=[
        subroutine_0x3573AC,
    ],
)

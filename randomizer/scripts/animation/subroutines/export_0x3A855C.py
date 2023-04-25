# pylint: disable=C0301,C0103

"""exports subroutine 0X3A855C"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3A855C,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A855C import (
    script as subroutine_0x3A855C,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A855C,
    start=0x3A855C,
    end=0x3A8579,
    scripts=[
        subroutine_0x3A855C,
    ],
)

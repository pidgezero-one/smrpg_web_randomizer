# pylint: disable=C0301,C0103

"""exports subroutine 0X3547FA"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3547FA,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3547FA import (
    script as subroutine_0x3547FA,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3547FA,
    start=0x3547FA,
    end=0x354891,
    scripts=[
        subroutine_0x3547FA,
    ],
)

# pylint: disable=C0301,C0103

"""exports subroutine 0X356754"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X356754,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x356754 import (
    script as subroutine_0x356754,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356754,
    start=0x356754,
    end=0x35678A,
    scripts=[
        subroutine_0x356754,
    ],
)

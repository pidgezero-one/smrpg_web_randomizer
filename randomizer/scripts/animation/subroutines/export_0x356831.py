# pylint: disable=C0301,C0103

"""exports subroutine 0X356831"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X356831,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x356831 import (
    script as subroutine_0x356831,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356831,
    start=0x356831,
    end=0x356918,
    scripts=[
        subroutine_0x356831,
    ],
)

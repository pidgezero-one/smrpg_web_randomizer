# pylint: disable=C0301,C0103

"""exports subroutine 0X356B4B"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X356B4B,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x356B4B import (
    script as subroutine_0x356B4B,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356B4B,
    start=0x356B4B,
    end=0x356B65,
    scripts=[
        subroutine_0x356B4B,
    ],
)

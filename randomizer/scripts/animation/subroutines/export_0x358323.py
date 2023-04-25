# pylint: disable=C0301,C0103

"""exports subroutine 0X358323"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X358323,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x358323 import (
    script as subroutine_0x358323,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X358323,
    start=0x358323,
    end=0x35837B,
    scripts=[
        subroutine_0x358323,
    ],
)

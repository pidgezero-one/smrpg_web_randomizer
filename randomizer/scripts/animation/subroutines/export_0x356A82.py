# pylint: disable=C0301,C0103

"""exports subroutine 0X356A82"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X356A82)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x356A82 import (
    script as subroutine_0x356A82)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356A82,
    start=0x356A82,
    end=0x356B14,
    scripts=[
        subroutine_0x356A82,
    ])

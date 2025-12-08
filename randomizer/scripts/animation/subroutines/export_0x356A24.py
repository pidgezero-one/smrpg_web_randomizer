# pylint: disable=C0301,C0103

"""exports subroutine 0X356A24"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X356A24)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x356A24 import (
    script as subroutine_0x356A24)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356A24,
    start=0x356A24,
    end=0x356A7D,
    scripts=[
        subroutine_0x356A24,
    ])

# pylint: disable=C0301,C0103

"""exports subroutine 0X356100"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X356100)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x356100 import (
    script as subroutine_0x356100)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356100,
    start=0x356100,
    end=0x356130,
    scripts=[
        subroutine_0x356100,
    ])

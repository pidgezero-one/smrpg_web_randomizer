# pylint: disable=C0301,C0103

"""exports subroutine 0X356EB6"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X356EB6)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x356EB6 import (
    script as subroutine_0x356EB6)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356EB6,
    start=0x356EB6,
    end=0x356F14,
    scripts=[
        subroutine_0x356EB6,
    ])

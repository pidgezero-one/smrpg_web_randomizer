# pylint: disable=C0301,C0103

"""exports subroutine 0X3580B4"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3580B4)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3580B4 import (
    script as subroutine_0x3580B4)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3580B4,
    start=0x3580B4,
    end=0x358132,
    scripts=[
        subroutine_0x3580B4,
    ])

# pylint: disable=C0301,C0103

"""exports subroutine 0X3527D0"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3527D0)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3527D0 import (
    script as subroutine_0x3527D0)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3527D0,
    start=0x3527D0,
    end=0x3527D9,
    scripts=[
        subroutine_0x3527D0,
    ])

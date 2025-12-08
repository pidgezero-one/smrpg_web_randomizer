# pylint: disable=C0301,C0103

"""exports subroutine 0X3523C4"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3523C4)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3523C4 import (
    script as subroutine_0x3523C4)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3523C4,
    start=0x3523C4,
    end=0x3523FC,
    scripts=[
        subroutine_0x3523C4,
    ])

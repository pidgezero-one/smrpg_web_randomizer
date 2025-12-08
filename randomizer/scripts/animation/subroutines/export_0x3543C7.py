# pylint: disable=C0301,C0103

"""exports subroutine 0X3543C7"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3543C7)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3543C7 import (
    script as subroutine_0x3543C7)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3543C7,
    start=0x3543C7,
    end=0x35458B,
    scripts=[
        subroutine_0x3543C7,
    ])

# pylint: disable=C0301,C0103

"""exports subroutine 0X359252"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X359252)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x359252 import (
    script as subroutine_0x359252)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X359252,
    start=0x359252,
    end=0x359396,
    scripts=[
        subroutine_0x359252,
    ])

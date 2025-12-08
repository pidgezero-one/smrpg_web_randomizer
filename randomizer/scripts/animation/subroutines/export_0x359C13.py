# pylint: disable=C0301,C0103

"""exports subroutine 0X359C13"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X359C13)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x359C13 import (
    script as subroutine_0x359C13)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X359C13,
    start=0x359C13,
    end=0x359E0A,
    scripts=[
        subroutine_0x359C13,
    ])

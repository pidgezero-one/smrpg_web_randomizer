# pylint: disable=C0301,C0103

"""exports subroutine 0X3586BD"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3586BD)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3586BD import (
    script as subroutine_0x3586BD)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3586BD,
    start=0x3586BD,
    end=0x3588DE,
    scripts=[
        subroutine_0x3586BD,
    ])

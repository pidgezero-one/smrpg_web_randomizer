# pylint: disable=C0301,C0103

"""exports subroutine 0X3A7999"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3A7999)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A7999 import (
    script as subroutine_0x3A7999)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A7999,
    start=0x3A7999,
    end=0x3A79A0,
    scripts=[
        subroutine_0x3A7999,
    ])

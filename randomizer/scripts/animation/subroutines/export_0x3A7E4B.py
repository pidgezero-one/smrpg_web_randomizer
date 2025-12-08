# pylint: disable=C0301,C0103

"""exports subroutine 0X3A7E4B"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3A7E4B)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A7E4B import (
    script as subroutine_0x3A7E4B)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A7E4B,
    start=0x3A7E4B,
    end=0x3A7E5C,
    scripts=[
        subroutine_0x3A7E4B,
    ])

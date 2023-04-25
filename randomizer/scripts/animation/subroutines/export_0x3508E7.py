# pylint: disable=C0301,C0103

"""exports subroutine 0X3508E7"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3508E7,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3508E7 import (
    script as subroutine_0x3508E7,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3508E7,
    start=0x3508E7,
    end=0x3508E7,
    scripts=[
        subroutine_0x3508E7,
    ],
)

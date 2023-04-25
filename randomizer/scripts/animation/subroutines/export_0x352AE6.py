# pylint: disable=C0301,C0103

"""exports subroutine 0X352AE6"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X352AE6,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x352AE6 import (
    script as subroutine_0x352AE6,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X352AE6,
    start=0x352AE6,
    end=0x352AED,
    scripts=[
        subroutine_0x352AE6,
    ],
)

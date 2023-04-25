# pylint: disable=C0301,C0103

"""exports subroutine 0X352E01"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X352E01,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x352E01 import (
    script as subroutine_0x352E01,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X352E01,
    start=0x352E01,
    end=0x352E09,
    scripts=[
        subroutine_0x352E01,
    ],
)

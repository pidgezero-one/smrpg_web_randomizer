# pylint: disable=C0301,C0103

"""exports subroutine 0X3563E5"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3563E5,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3563E5 import (
    script as subroutine_0x3563E5,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3563E5,
    start=0x3563E5,
    end=0x356455,
    scripts=[
        subroutine_0x3563E5,
    ],
)

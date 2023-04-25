# pylint: disable=C0301,C0103

"""exports subroutine 0X3556ED"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3556ED,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3556ED import (
    script as subroutine_0x3556ED,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3556ED,
    start=0x3556ED,
    end=0x3557C5,
    scripts=[
        subroutine_0x3556ED,
    ],
)

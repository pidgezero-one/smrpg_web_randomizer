# pylint: disable=C0301,C0103

"""exports subroutine 0X35F9B4"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35F9B4,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35F9B4 import (
    script as subroutine_0x35F9B4,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F9B4,
    start=0x35F9B4,
    end=0x35FA94,
    scripts=[
        subroutine_0x35F9B4,
    ],
)

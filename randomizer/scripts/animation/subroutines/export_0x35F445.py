# pylint: disable=C0301,C0103

"""exports subroutine 0X35F445"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35F445,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35F445 import (
    script as subroutine_0x35F445,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F445,
    start=0x35F445,
    end=0x35F49D,
    scripts=[
        subroutine_0x35F445,
    ],
)

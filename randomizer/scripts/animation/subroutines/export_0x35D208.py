# pylint: disable=C0301,C0103

"""exports subroutine 0X35D208"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35D208,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35D208 import (
    script as subroutine_0x35D208,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35D208,
    start=0x35D208,
    end=0x35D2D4,
    scripts=[
        subroutine_0x35D208,
    ],
)

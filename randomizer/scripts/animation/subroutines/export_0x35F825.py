# pylint: disable=C0301,C0103

"""exports subroutine 0X35F825"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35F825,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35F825 import (
    script as subroutine_0x35F825,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F825,
    start=0x35F825,
    end=0x35F92B,
    scripts=[
        subroutine_0x35F825,
    ],
)

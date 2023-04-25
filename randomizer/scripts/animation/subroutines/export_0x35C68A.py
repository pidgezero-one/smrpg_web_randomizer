# pylint: disable=C0301,C0103

"""exports subroutine 0X35C68A"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35C68A,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35C68A import (
    script as subroutine_0x35C68A,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35C68A,
    start=0x35C68A,
    end=0x35C711,
    scripts=[
        subroutine_0x35C68A,
    ],
)

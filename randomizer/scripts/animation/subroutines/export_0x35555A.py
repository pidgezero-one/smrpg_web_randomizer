# pylint: disable=C0301,C0103

"""exports subroutine 0X35555A"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35555A,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35555A import (
    script as subroutine_0x35555A,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35555A,
    start=0x35555A,
    end=0x3555B5,
    scripts=[
        subroutine_0x35555A,
    ],
)

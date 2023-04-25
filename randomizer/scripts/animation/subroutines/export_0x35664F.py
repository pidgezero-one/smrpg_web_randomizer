# pylint: disable=C0301,C0103

"""exports subroutine 0X35664F"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35664F,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35664F import (
    script as subroutine_0x35664F,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35664F,
    start=0x35664F,
    end=0x3566BE,
    scripts=[
        subroutine_0x35664F,
    ],
)

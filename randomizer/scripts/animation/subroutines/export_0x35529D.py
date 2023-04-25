# pylint: disable=C0301,C0103

"""exports subroutine 0X35529D"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35529D,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35529D import (
    script as subroutine_0x35529D,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35529D,
    start=0x35529D,
    end=0x3552C4,
    scripts=[
        subroutine_0x35529D,
    ],
)

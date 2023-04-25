# pylint: disable=C0301,C0103

"""exports subroutine 0X355BD4"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X355BD4,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x355BD4 import (
    script as subroutine_0x355BD4,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X355BD4,
    start=0x355BD4,
    end=0x355DB5,
    scripts=[
        subroutine_0x355BD4,
    ],
)

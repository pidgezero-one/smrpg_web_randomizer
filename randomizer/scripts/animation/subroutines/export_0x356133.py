# pylint: disable=C0301,C0103

"""exports subroutine 0X356133"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X356133,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x356133 import (
    script as subroutine_0x356133,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356133,
    start=0x356133,
    end=0x356151,
    scripts=[
        subroutine_0x356133,
    ],
)

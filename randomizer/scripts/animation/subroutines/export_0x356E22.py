# pylint: disable=C0301,C0103

"""exports subroutine 0X356E22"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X356E22,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x356E22 import (
    script as subroutine_0x356E22,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356E22,
    start=0x356E22,
    end=0x356EAF,
    scripts=[
        subroutine_0x356E22,
    ],
)

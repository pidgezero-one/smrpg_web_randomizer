# pylint: disable=C0301,C0103

"""exports subroutine 0X356078"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X356078,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x356078 import (
    script as subroutine_0x356078,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356078,
    start=0x356078,
    end=0x356086,
    scripts=[
        subroutine_0x356078,
    ],
)

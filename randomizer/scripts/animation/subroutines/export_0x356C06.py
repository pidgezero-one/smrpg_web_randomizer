# pylint: disable=C0301,C0103

"""exports subroutine 0X356C06"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X356C06,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x356C06 import (
    script as subroutine_0x356C06,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356C06,
    start=0x356C06,
    end=0x356C87,
    scripts=[
        subroutine_0x356C06,
    ],
)

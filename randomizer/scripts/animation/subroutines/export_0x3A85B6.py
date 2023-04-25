# pylint: disable=C0301,C0103

"""exports subroutine 0X3A85B6"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3A85B6,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A85B6 import (
    script as subroutine_0x3A85B6,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A85B6,
    start=0x3A85B6,
    end=0x3A85BF,
    scripts=[
        subroutine_0x3A85B6,
    ],
)

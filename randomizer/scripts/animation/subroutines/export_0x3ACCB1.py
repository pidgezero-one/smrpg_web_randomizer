# pylint: disable=C0301,C0103

"""exports subroutine 0X3ACCB1"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3ACCB1,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3ACCB1 import (
    script as subroutine_0x3ACCB1,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3ACCB1,
    start=0x3ACCB1,
    end=0x3ACF43,
    scripts=[
        subroutine_0x3ACCB1,
    ],
)

# pylint: disable=C0301,C0103

"""exports subroutine 0X3A986A"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3A986A,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A986A import (
    script as subroutine_0x3A986A,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A986A,
    start=0x3A986A,
    end=0x3A9D74,
    scripts=[
        subroutine_0x3A986A,
    ],
)

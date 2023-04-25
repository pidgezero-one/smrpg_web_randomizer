# pylint: disable=C0301,C0103

"""exports subroutine 0X3A78B8"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3A78B8,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A78B8 import (
    script as subroutine_0x3A78B8,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A78B8,
    start=0x3A78B8,
    end=0x3A78C0,
    scripts=[
        subroutine_0x3A78B8,
    ],
)

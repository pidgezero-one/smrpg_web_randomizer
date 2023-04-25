# pylint: disable=C0301,C0103

"""exports subroutine 0X350A21"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X350A21,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x350A21 import (
    script as subroutine_0x350A21,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X350A21,
    start=0x350A21,
    end=0x350A37,
    scripts=[
        subroutine_0x350A21,
    ],
)

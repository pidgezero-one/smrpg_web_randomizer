# pylint: disable=C0301,C0103

"""exports subroutine 0X354D07"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X354D07,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x354D07 import (
    script as subroutine_0x354D07,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X354D07,
    start=0x354D07,
    end=0x354E00,
    scripts=[
        subroutine_0x354D07,
    ],
)

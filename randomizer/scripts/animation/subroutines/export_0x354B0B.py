# pylint: disable=C0301,C0103

"""exports subroutine 0X354B0B"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X354B0B,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x354B0B import (
    script as subroutine_0x354B0B,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X354B0B,
    start=0x354B0B,
    end=0x354B30,
    scripts=[
        subroutine_0x354B0B,
    ],
)

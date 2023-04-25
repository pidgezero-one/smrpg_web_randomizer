# pylint: disable=C0301,C0103

"""exports subroutine 0X354E1F"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X354E1F,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x354E1F import (
    script as subroutine_0x354E1F,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X354E1F,
    start=0x354E1F,
    end=0x354E6B,
    scripts=[
        subroutine_0x354E1F,
    ],
)

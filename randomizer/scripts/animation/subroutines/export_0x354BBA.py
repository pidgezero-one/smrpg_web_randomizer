# pylint: disable=C0301,C0103

"""exports subroutine 0X354BBA"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X354BBA,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x354BBA import (
    script as subroutine_0x354BBA,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X354BBA,
    start=0x354BBA,
    end=0x354C83,
    scripts=[
        subroutine_0x354BBA,
    ],
)

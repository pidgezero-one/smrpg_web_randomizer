# pylint: disable=C0301,C0103

"""exports subroutine 0X358C8F"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X358C8F,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x358C8F import (
    script as subroutine_0x358C8F,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X358C8F,
    start=0x358C8F,
    end=0x35924B,
    scripts=[
        subroutine_0x358C8F,
    ],
)

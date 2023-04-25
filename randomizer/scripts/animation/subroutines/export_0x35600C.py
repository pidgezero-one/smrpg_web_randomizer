# pylint: disable=C0301,C0103

"""exports subroutine 0X35600C"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35600C,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35600C import (
    script as subroutine_0x35600C,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35600C,
    start=0x35600C,
    end=0x356040,
    scripts=[
        subroutine_0x35600C,
    ],
)

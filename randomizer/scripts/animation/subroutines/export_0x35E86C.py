# pylint: disable=C0301,C0103

"""exports subroutine 0X35E86C"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35E86C,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35E86C import (
    script as subroutine_0x35E86C,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35E86C,
    start=0x35E86C,
    end=0x35E9C2,
    scripts=[
        subroutine_0x35E86C,
    ],
)

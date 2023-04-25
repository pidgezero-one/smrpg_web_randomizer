# pylint: disable=C0301,C0103

"""exports subroutine 0X3597F7"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3597F7,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3597F7 import (
    script as subroutine_0x3597F7,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3597F7,
    start=0x3597F7,
    end=0x3599E5,
    scripts=[
        subroutine_0x3597F7,
    ],
)

# pylint: disable=C0301,C0103

"""exports subroutine 0X3A7CCA"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3A7CCA,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A7CCA import (
    script as subroutine_0x3A7CCA,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A7CCA,
    start=0x3A7CCA,
    end=0x3A7CD1,
    scripts=[
        subroutine_0x3A7CCA,
    ],
)

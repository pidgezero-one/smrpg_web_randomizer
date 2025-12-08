# pylint: disable=C0301,C0103

"""exports subroutine 0X353AE1"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X353AE1)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x353AE1 import (
    script as subroutine_0x353AE1)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X353AE1,
    start=0x353AE1,
    end=0x353C6F,
    scripts=[
        subroutine_0x353AE1,
    ])

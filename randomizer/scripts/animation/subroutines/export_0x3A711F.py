# pylint: disable=C0301,C0103

"""exports subroutine 0X3A711F"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3A711F)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A711F import (
    script as subroutine_0x3A711F)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A711F,
    start=0x3A711F,
    end=0x3A715C,
    scripts=[
        subroutine_0x3A711F,
    ])

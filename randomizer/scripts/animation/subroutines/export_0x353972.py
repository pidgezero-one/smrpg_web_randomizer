# pylint: disable=C0301,C0103

"""exports subroutine 0X353972"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X353972)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x353972 import (
    script as subroutine_0x353972)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X353972,
    start=0x353972,
    end=0x353ACE,
    scripts=[
        subroutine_0x353972,
    ])

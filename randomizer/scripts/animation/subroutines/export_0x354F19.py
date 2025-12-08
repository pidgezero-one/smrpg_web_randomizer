# pylint: disable=C0301,C0103

"""exports subroutine 0X354F19"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X354F19)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x354F19 import (
    script as subroutine_0x354F19)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X354F19,
    start=0x354F19,
    end=0x354FC3,
    scripts=[
        subroutine_0x354F19,
    ])

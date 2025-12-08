# pylint: disable=C0301,C0103

"""exports subroutine 0X354A24"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X354A24)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x354A24 import (
    script as subroutine_0x354A24)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X354A24,
    start=0x354A24,
    end=0x354AF3,
    scripts=[
        subroutine_0x354A24,
    ])

# pylint: disable=C0301,C0103

"""exports subroutine 0X351595"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X351595)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x351595 import (
    script as subroutine_0x351595)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X351595,
    start=0x351595,
    end=0x352127,
    scripts=[
        subroutine_0x351595,
    ])

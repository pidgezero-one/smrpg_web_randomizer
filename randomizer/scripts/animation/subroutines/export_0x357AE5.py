# pylint: disable=C0301,C0103

"""exports subroutine 0X357AE5"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X357AE5)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x357AE5 import (
    script as subroutine_0x357AE5)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X357AE5,
    start=0x357AE5,
    end=0x357B71,
    scripts=[
        subroutine_0x357AE5,
    ])

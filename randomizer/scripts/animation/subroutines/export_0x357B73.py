# pylint: disable=C0301,C0103

"""exports subroutine 0X357B73"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X357B73)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x357B73 import (
    script as subroutine_0x357B73)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X357B73,
    start=0x357B73,
    end=0x357C43,
    scripts=[
        subroutine_0x357B73,
    ])

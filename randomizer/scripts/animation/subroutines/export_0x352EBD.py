# pylint: disable=C0301,C0103

"""exports subroutine 0X352EBD"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X352EBD)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x352EBD import (
    script as subroutine_0x352EBD)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X352EBD,
    start=0x352EBD,
    end=0x352ECE,
    scripts=[
        subroutine_0x352EBD,
    ])

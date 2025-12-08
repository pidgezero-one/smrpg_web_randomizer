# pylint: disable=C0301,C0103

"""exports subroutine 0X359F2C"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X359F2C)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x359F2C import (
    script as subroutine_0x359F2C)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X359F2C,
    start=0x359F2C,
    end=0x35A0A4,
    scripts=[
        subroutine_0x359F2C,
    ])

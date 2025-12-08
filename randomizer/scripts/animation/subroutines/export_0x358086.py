# pylint: disable=C0301,C0103

"""exports subroutine 0X358086"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X358086)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x358086 import (
    script as subroutine_0x358086)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X358086,
    start=0x358086,
    end=0x35809C,
    scripts=[
        subroutine_0x358086,
    ])

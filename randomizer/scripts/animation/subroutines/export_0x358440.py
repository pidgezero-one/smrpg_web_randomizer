# pylint: disable=C0301,C0103

"""exports subroutine 0X358440"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X358440)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x358440 import (
    script as subroutine_0x358440)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X358440,
    start=0x358440,
    end=0x358498,
    scripts=[
        subroutine_0x358440,
    ])

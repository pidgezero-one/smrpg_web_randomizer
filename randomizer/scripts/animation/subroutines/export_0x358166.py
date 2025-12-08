# pylint: disable=C0301,C0103

"""exports subroutine 0X358166"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X358166)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x358166 import (
    script as subroutine_0x358166)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X358166,
    start=0x358166,
    end=0x35816A,
    scripts=[
        subroutine_0x358166,
    ])

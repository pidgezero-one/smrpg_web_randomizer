# pylint: disable=C0301,C0103

"""exports subroutine 0X3A8264"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3A8264)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A8264 import (
    script as subroutine_0x3A8264)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A8264,
    start=0x3A8264,
    end=0x3A826D,
    scripts=[
        subroutine_0x3A8264,
    ])

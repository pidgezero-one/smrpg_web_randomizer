# pylint: disable=C0301,C0103

"""exports subroutine 0X359E17"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X359E17)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x359E17 import (
    script as subroutine_0x359E17)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X359E17,
    start=0x359E17,
    end=0x359F19,
    scripts=[
        subroutine_0x359E17,
    ])

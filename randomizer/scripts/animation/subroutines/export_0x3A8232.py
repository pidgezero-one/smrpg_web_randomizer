# pylint: disable=C0301,C0103

"""exports subroutine 0X3A8232"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3A8232)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A8232 import (
    script as subroutine_0x3A8232)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A8232,
    start=0x3A8232,
    end=0x3A823B,
    scripts=[
        subroutine_0x3A8232,
    ])

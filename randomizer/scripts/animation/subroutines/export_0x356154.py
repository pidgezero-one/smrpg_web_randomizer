# pylint: disable=C0301,C0103

"""exports subroutine 0X356154"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X356154)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x356154 import (
    script as subroutine_0x356154)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356154,
    start=0x356154,
    end=0x356179,
    scripts=[
        subroutine_0x356154,
    ])

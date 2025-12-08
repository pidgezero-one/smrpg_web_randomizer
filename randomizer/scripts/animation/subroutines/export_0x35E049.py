# pylint: disable=C0301,C0103

"""exports subroutine 0X35E049"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35E049)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35E049 import (
    script as subroutine_0x35E049)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35E049,
    start=0x35E049,
    end=0x35E07B,
    scripts=[
        subroutine_0x35E049,
    ])

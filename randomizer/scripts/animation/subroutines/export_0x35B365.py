# pylint: disable=C0301,C0103

"""exports subroutine 0X35B365"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35B365)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35B365 import (
    script as subroutine_0x35B365)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35B365,
    start=0x35B365,
    end=0x35B43C,
    scripts=[
        subroutine_0x35B365,
    ])

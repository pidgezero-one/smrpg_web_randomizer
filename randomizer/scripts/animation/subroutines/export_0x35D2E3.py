# pylint: disable=C0301,C0103

"""exports subroutine 0X35D2E3"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35D2E3)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35D2E3 import (
    script as subroutine_0x35D2E3)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35D2E3,
    start=0x35D2E3,
    end=0x35D38D,
    scripts=[
        subroutine_0x35D2E3,
    ])

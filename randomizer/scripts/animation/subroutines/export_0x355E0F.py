# pylint: disable=C0301,C0103

"""exports subroutine 0X355E0F"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X355E0F)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x355E0F import (
    script as subroutine_0x355E0F)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X355E0F,
    start=0x355E0F,
    end=0x355F1C,
    scripts=[
        subroutine_0x355E0F,
    ])

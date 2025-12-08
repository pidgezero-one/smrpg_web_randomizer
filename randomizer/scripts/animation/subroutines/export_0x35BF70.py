# pylint: disable=C0301,C0103

"""exports subroutine 0X35BF70"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35BF70)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35BF70 import (
    script as subroutine_0x35BF70)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35BF70,
    start=0x35BF70,
    end=0x35C123,
    scripts=[
        subroutine_0x35BF70,
    ])

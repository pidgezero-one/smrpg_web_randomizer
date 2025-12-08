# pylint: disable=C0301,C0103

"""exports subroutine 0X35C604"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35C604)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35C604 import (
    script as subroutine_0x35C604)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35C604,
    start=0x35C604,
    end=0x35C685,
    scripts=[
        subroutine_0x35C604,
    ])

# pylint: disable=C0301,C0103

"""exports subroutine 0X35AC50"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35AC50)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35AC50 import (
    script as subroutine_0x35AC50)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35AC50,
    start=0x35AC50,
    end=0x35AC58,
    scripts=[
        subroutine_0x35AC50,
    ])

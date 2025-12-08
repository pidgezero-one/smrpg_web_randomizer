# pylint: disable=C0301,C0103

"""exports subroutine 0X356043"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X356043)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x356043 import (
    script as subroutine_0x356043)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356043,
    start=0x356043,
    end=0x35605E,
    scripts=[
        subroutine_0x356043,
    ])

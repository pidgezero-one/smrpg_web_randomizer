# pylint: disable=C0301,C0103

"""exports subroutine 0X35A4FB"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35A4FB)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35A4FB import (
    script as subroutine_0x35A4FB)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35A4FB,
    start=0x35A4FB,
    end=0x35A69F,
    scripts=[
        subroutine_0x35A4FB,
    ])

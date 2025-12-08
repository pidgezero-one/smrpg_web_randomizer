# pylint: disable=C0301,C0103

"""exports subroutine 0X3A82FA"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3A82FA)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A82FA import (
    script as subroutine_0x3A82FA)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A82FA,
    start=0x3A82FA,
    end=0x3A8303,
    scripts=[
        subroutine_0x3A82FA,
    ])

# pylint: disable=C0301,C0103

"""exports subroutine 0X35F397"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35F397,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35F397 import (
    script as subroutine_0x35F397,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F397,
    start=0x35F397,
    end=0x35F3E7,
    scripts=[
        subroutine_0x35F397,
    ],
)

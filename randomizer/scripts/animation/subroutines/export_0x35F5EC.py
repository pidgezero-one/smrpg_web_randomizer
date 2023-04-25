# pylint: disable=C0301,C0103

"""exports subroutine 0X35F5EC"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35F5EC,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35F5EC import (
    script as subroutine_0x35F5EC,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F5EC,
    start=0x35F5EC,
    end=0x35F729,
    scripts=[
        subroutine_0x35F5EC,
    ],
)

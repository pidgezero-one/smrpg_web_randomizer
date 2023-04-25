# pylint: disable=C0301,C0103

"""exports subroutine 0X35F219"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35F219,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35F219 import (
    script as subroutine_0x35F219,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F219,
    start=0x35F219,
    end=0x35F262,
    scripts=[
        subroutine_0x35F219,
    ],
)

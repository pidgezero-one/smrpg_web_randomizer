# pylint: disable=C0301,C0103

"""exports subroutine 0X35F13F"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35F13F,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35F13F import (
    script as subroutine_0x35F13F,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F13F,
    start=0x35F13F,
    end=0x35F1BD,
    scripts=[
        subroutine_0x35F13F,
    ],
)

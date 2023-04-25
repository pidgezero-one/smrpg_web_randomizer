# pylint: disable=C0301,C0103

"""exports subroutine 0X35BBED"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35BBED,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35BBED import (
    script as subroutine_0x35BBED,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35BBED,
    start=0x35BBED,
    end=0x35BE03,
    scripts=[
        subroutine_0x35BBED,
    ],
)

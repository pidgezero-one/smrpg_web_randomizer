# pylint: disable=C0301,C0103

"""exports subroutine 0X35BA9B"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35BA9B,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35BA9B import (
    script as subroutine_0x35BA9B,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35BA9B,
    start=0x35BA9B,
    end=0x35BBC6,
    scripts=[
        subroutine_0x35BA9B,
    ],
)

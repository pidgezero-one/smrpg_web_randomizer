# pylint: disable=C0301,C0103

"""exports subroutine 0X35C29D"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35C29D,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35C29D import (
    script as subroutine_0x35C29D,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35C29D,
    start=0x35C29D,
    end=0x35C2DC,
    scripts=[
        subroutine_0x35C29D,
    ],
)

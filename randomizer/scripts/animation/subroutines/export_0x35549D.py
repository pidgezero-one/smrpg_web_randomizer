# pylint: disable=C0301,C0103

"""exports subroutine 0X35549D"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35549D,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35549D import (
    script as subroutine_0x35549D,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35549D,
    start=0x35549D,
    end=0x35554D,
    scripts=[
        subroutine_0x35549D,
    ],
)

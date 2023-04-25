# pylint: disable=C0301,C0103

"""exports subroutine 0X35B9B2"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35B9B2,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35B9B2 import (
    script as subroutine_0x35B9B2,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35B9B2,
    start=0x35B9B2,
    end=0x35BA90,
    scripts=[
        subroutine_0x35B9B2,
    ],
)

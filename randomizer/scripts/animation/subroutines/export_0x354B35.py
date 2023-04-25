# pylint: disable=C0301,C0103

"""exports subroutine 0X354B35"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X354B35,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x354B35 import (
    script as subroutine_0x354B35,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X354B35,
    start=0x354B35,
    end=0x354BB3,
    scripts=[
        subroutine_0x354B35,
    ],
)

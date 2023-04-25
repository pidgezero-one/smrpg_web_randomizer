# pylint: disable=C0301,C0103

"""exports subroutine 0X35A3A1"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35A3A1,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35A3A1 import (
    script as subroutine_0x35A3A1,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35A3A1,
    start=0x35A3A1,
    end=0x35A3B7,
    scripts=[
        subroutine_0x35A3A1,
    ],
)

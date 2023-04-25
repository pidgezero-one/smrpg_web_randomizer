# pylint: disable=C0301,C0103

"""exports subroutine 0X35A4DE"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35A4DE,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35A4DE import (
    script as subroutine_0x35A4DE,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35A4DE,
    start=0x35A4DE,
    end=0x35A4E6,
    scripts=[
        subroutine_0x35A4DE,
    ],
)

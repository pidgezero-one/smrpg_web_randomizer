# pylint: disable=C0301,C0103

"""exports subroutine 0X35240C"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35240C,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35240C import (
    script as subroutine_0x35240C,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35240C,
    start=0x35240C,
    end=0x352456,
    scripts=[
        subroutine_0x35240C,
    ],
)

# pylint: disable=C0301,C0103

"""exports subroutine 0X35617C"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35617C,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35617C import (
    script as subroutine_0x35617C,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35617C,
    start=0x35617C,
    end=0x3561AC,
    scripts=[
        subroutine_0x35617C,
    ],
)

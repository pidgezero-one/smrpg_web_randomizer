# pylint: disable=C0301,C0103

"""exports subroutine 0X35DCB6"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35DCB6,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35DCB6 import (
    script as subroutine_0x35DCB6,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35DCB6,
    start=0x35DCB6,
    end=0x35DCD4,
    scripts=[
        subroutine_0x35DCB6,
    ],
)

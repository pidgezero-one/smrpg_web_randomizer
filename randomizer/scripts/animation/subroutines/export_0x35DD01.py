# pylint: disable=C0301,C0103

"""exports subroutine 0X35DD01"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35DD01,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35DD01 import (
    script as subroutine_0x35DD01,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35DD01,
    start=0x35DD01,
    end=0x35DFC7,
    scripts=[
        subroutine_0x35DD01,
    ],
)

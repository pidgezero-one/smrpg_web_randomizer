# pylint: disable=C0301,C0103

"""exports subroutine 0X35C307"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35C307,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35C307 import (
    script as subroutine_0x35C307,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35C307,
    start=0x35C307,
    end=0x35C362,
    scripts=[
        subroutine_0x35C307,
    ],
)

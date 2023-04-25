# pylint: disable=C0301,C0103

"""exports subroutine 0X35C968"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35C968,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35C968 import (
    script as subroutine_0x35C968,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35C968,
    start=0x35C968,
    end=0x35C991,
    scripts=[
        subroutine_0x35C968,
    ],
)

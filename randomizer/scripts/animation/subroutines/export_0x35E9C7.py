# pylint: disable=C0301,C0103

"""exports subroutine 0X35E9C7"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35E9C7)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35E9C7 import (
    script as subroutine_0x35E9C7)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35E9C7,
    start=0x35E9C7,
    end=0x35EA0B,
    scripts=[
        subroutine_0x35E9C7,
    ])

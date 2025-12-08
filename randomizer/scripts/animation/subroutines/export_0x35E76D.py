# pylint: disable=C0301,C0103

"""exports subroutine 0X35E76D"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35E76D)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35E76D import (
    script as subroutine_0x35E76D)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35E76D,
    start=0x35E76D,
    end=0x35E865,
    scripts=[
        subroutine_0x35E76D,
    ])

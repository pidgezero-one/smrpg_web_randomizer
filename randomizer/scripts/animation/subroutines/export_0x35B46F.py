# pylint: disable=C0301,C0103

"""exports subroutine 0X35B46F"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35B46F)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35B46F import (
    script as subroutine_0x35B46F)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35B46F,
    start=0x35B46F,
    end=0x35B5FF,
    scripts=[
        subroutine_0x35B46F,
    ])

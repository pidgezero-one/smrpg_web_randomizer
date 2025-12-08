# pylint: disable=C0301,C0103

"""exports subroutine 0X3A88FF"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3A88FF)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A88FF import (
    script as subroutine_0x3A88FF)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A88FF,
    start=0x3A88FF,
    end=0x3A8A67,
    scripts=[
        subroutine_0x3A88FF,
    ])

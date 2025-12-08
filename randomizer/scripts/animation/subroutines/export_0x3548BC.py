# pylint: disable=C0301,C0103

"""exports subroutine 0X3548BC"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3548BC)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3548BC import (
    script as subroutine_0x3548BC)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3548BC,
    start=0x3548BC,
    end=0x3548F3,
    scripts=[
        subroutine_0x3548BC,
    ])

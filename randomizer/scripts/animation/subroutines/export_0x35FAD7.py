# pylint: disable=C0301,C0103

"""exports subroutine 0X35FAD7"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35FAD7)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35FAD7 import (
    script as subroutine_0x35FAD7)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35FAD7,
    start=0x35FAD7,
    end=0x35FC88,
    scripts=[
        subroutine_0x35FAD7,
    ])

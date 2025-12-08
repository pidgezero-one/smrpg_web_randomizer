# pylint: disable=C0301,C0103

"""exports subroutine 0X3AC7CF"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3AC7CF)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3AC7CF import (
    script as subroutine_0x3AC7CF)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3AC7CF,
    start=0x3AC7CF,
    end=0x3ACCAF,
    scripts=[
        subroutine_0x3AC7CF,
    ])

# pylint: disable=C0301,C0103

"""exports subroutine 0X3559FC"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3559FC)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3559FC import (
    script as subroutine_0x3559FC)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3559FC,
    start=0x3559FC,
    end=0x355AD8,
    scripts=[
        subroutine_0x3559FC,
    ])

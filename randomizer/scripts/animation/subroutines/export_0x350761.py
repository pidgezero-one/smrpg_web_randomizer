# pylint: disable=C0301,C0103

"""exports subroutine 0X350761"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X350761)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x350761 import (
    script as subroutine_0x350761)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X350761,
    start=0x350761,
    end=0x350761,
    scripts=[
        subroutine_0x350761,
    ])

# pylint: disable=C0301,C0103

"""exports subroutine 0X3A72CE"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3A72CE)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A72CE import (
    script as subroutine_0x3A72CE)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A72CE,
    start=0x3A72CE,
    end=0x3A7327,
    scripts=[
        subroutine_0x3A72CE,
    ])

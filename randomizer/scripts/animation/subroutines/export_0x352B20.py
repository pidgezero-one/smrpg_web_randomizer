# pylint: disable=C0301,C0103

"""exports subroutine 0X352B20"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X352B20)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x352B20 import (
    script as subroutine_0x352B20)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X352B20,
    start=0x352B20,
    end=0x352B28,
    scripts=[
        subroutine_0x352B20,
    ])

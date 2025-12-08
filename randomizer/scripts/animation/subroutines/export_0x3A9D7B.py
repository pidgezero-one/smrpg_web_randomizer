# pylint: disable=C0301,C0103

"""exports subroutine 0X3A9D7B"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3A9D7B)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A9D7B import (
    script as subroutine_0x3A9D7B)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A9D7B,
    start=0x3A9D7B,
    end=0x3A9EB6,
    scripts=[
        subroutine_0x3A9D7B,
    ])

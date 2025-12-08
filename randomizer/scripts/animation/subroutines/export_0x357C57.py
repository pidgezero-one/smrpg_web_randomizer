# pylint: disable=C0301,C0103

"""exports subroutine 0X357C57"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X357C57)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x357C57 import (
    script as subroutine_0x357C57)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X357C57,
    start=0x357C57,
    end=0x357CF5,
    scripts=[
        subroutine_0x357C57,
    ])

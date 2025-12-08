# pylint: disable=C0301,C0103

"""exports subroutine 0X3A9725"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3A9725)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A9725 import (
    script as subroutine_0x3A9725)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A9725,
    start=0x3A9725,
    end=0x3A97CD,
    scripts=[
        subroutine_0x3A9725,
    ])

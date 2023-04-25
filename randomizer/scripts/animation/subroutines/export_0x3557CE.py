# pylint: disable=C0301,C0103

"""exports subroutine 0X3557CE"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3557CE,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3557CE import (
    script as subroutine_0x3557CE,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3557CE,
    start=0x3557CE,
    end=0x3558A7,
    scripts=[
        subroutine_0x3557CE,
    ],
)

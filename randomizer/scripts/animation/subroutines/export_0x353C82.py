# pylint: disable=C0301,C0103

"""exports subroutine 0X353C82"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X353C82,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x353C82 import (
    script as subroutine_0x353C82,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X353C82,
    start=0x353C82,
    end=0x353DCB,
    scripts=[
        subroutine_0x353C82,
    ],
)

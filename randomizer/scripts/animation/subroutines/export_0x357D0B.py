# pylint: disable=C0301,C0103

"""exports subroutine 0X357D0B"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X357D0B,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x357D0B import (
    script as subroutine_0x357D0B,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X357D0B,
    start=0x357D0B,
    end=0x357F73,
    scripts=[
        subroutine_0x357D0B,
    ],
)

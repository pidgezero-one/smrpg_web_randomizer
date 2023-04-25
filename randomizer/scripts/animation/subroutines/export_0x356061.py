# pylint: disable=C0301,C0103

"""exports subroutine 0X356061"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X356061,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x356061 import (
    script as subroutine_0x356061,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356061,
    start=0x356061,
    end=0x356075,
    scripts=[
        subroutine_0x356061,
    ],
)

# pylint: disable=C0301,C0103

"""exports subroutine 0X354E72"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X354E72,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x354E72 import (
    script as subroutine_0x354E72,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X354E72,
    start=0x354E72,
    end=0x354F10,
    scripts=[
        subroutine_0x354E72,
    ],
)

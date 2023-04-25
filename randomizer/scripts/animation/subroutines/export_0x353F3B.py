# pylint: disable=C0301,C0103

"""exports subroutine 0X353F3B"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X353F3B,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x353F3B import (
    script as subroutine_0x353F3B,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X353F3B,
    start=0x353F3B,
    end=0x353F6A,
    scripts=[
        subroutine_0x353F3B,
    ],
)

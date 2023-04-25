# pylint: disable=C0301,C0103

"""exports subroutine 0X3576BE"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3576BE,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3576BE import (
    script as subroutine_0x3576BE,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3576BE,
    start=0x3576BE,
    end=0x3578B3,
    scripts=[
        subroutine_0x3576BE,
    ],
)

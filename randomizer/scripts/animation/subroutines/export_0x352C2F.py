# pylint: disable=C0301,C0103

"""exports subroutine 0X352C2F"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X352C2F,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x352C2F import (
    script as subroutine_0x352C2F,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X352C2F,
    start=0x352C2F,
    end=0x352C40,
    scripts=[
        subroutine_0x352C2F,
    ],
)

# pylint: disable=C0301,C0103

"""exports subroutine 0X352CB2"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X352CB2,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x352CB2 import (
    script as subroutine_0x352CB2,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X352CB2,
    start=0x352CB2,
    end=0x352CBA,
    scripts=[
        subroutine_0x352CB2,
    ],
)

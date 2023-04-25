# pylint: disable=C0301,C0103

"""exports subroutine 0X35F4A2"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35F4A2,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35F4A2 import (
    script as subroutine_0x35F4A2,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F4A2,
    start=0x35F4A2,
    end=0x35F4A8,
    scripts=[
        subroutine_0x35F4A2,
    ],
)

# pylint: disable=C0301,C0103

"""exports subroutine 0X35ECEA"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35ECEA,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35ECEA import (
    script as subroutine_0x35ECEA,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35ECEA,
    start=0x35F112,
    end=0x35F123,
    scripts=[
        subroutine_0x35ECEA,
    ],
)

# pylint: disable=C0301,C0103

"""exports subroutine 0X35EA16"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35EA16,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35EA16 import (
    script as subroutine_0x35EA16,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35EA16,
    start=0x35EA16,
    end=0x35EAF8,
    scripts=[
        subroutine_0x35EA16,
    ],
)

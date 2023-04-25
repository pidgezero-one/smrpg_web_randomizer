# pylint: disable=C0301,C0103

"""exports subroutine 0X35DFCE"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35DFCE,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35DFCE import (
    script as subroutine_0x35DFCE,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35DFCE,
    start=0x35DFCE,
    end=0x35E044,
    scripts=[
        subroutine_0x35DFCE,
    ],
)

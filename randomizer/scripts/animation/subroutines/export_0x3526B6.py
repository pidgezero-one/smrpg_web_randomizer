# pylint: disable=C0301,C0103

"""exports subroutine 0X3526B6"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3526B6,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3526B6 import (
    script as subroutine_0x3526B6,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3526B6,
    start=0x3526B6,
    end=0x3526BD,
    scripts=[
        subroutine_0x3526B6,
    ],
)

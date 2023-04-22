# pylint: disable=C0301,C0103

"""exports subroutine 0X3AD703"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3AD703,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3AD703 import (
    script as subroutine_0x3AD703,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3AD703,
    start=0x3AD703,
    end=0x3AECF6,
    scripts=[
        subroutine_0x3AD703,
    ],
)

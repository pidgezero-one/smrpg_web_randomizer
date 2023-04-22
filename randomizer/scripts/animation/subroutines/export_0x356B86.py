# pylint: disable=C0301,C0103

"""exports subroutine 0X356B86"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X356B86,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x356B86 import (
    script as subroutine_0x356B86,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356B86,
    start=0x356B86,
    end=0x356BF1,
    scripts=[
        subroutine_0x356B86,
    ],
)

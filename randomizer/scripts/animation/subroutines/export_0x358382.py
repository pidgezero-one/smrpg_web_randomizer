# pylint: disable=C0301,C0103

"""exports subroutine 0X358382"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X358382,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x358382 import (
    script as subroutine_0x358382,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X358382,
    start=0x358382,
    end=0x3583DA,
    scripts=[
        subroutine_0x358382,
    ],
)

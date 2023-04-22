# pylint: disable=C0301,C0103

"""exports subroutine 0X3AA6A7"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3AA6A7,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3AA6A7 import (
    script as subroutine_0x3AA6A7,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3AA6A7,
    start=0x3AA6A7,
    end=0x3AA8EC,
    scripts=[
        subroutine_0x3AA6A7,
    ],
)

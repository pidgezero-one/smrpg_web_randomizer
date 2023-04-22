# pylint: disable=C0301,C0103

"""exports subroutine 0X351080"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X351080,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x351080 import (
    script as subroutine_0x351080,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X351080,
    start=0x351080,
    end=0x351492,
    scripts=[
        subroutine_0x351080,
    ],
)

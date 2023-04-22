# pylint: disable=C0301,C0103

"""exports subroutine 0X352D13"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X352D13,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x352D13 import (
    script as subroutine_0x352D13,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X352D13,
    start=0x352D13,
    end=0x352D1A,
    scripts=[
        subroutine_0x352D13,
    ],
)

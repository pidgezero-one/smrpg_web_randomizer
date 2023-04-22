# pylint: disable=C0301,C0103

"""exports subroutine 0X352E5F"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X352E5F,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x352E5F import (
    script as subroutine_0x352E5F,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X352E5F,
    start=0x352E5F,
    end=0x352E66,
    scripts=[
        subroutine_0x352E5F,
    ],
)

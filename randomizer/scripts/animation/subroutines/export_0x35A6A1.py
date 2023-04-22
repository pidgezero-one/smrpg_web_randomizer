# pylint: disable=C0301,C0103

"""exports subroutine 0X35A6A1"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35A6A1,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35A6A1 import (
    script as subroutine_0x35A6A1,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35A6A1,
    start=0x35A6A1,
    end=0x35A770,
    scripts=[
        subroutine_0x35A6A1,
    ],
)

# pylint: disable=C0301,C0103

"""exports subroutine 0X357604"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X357604,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x357604 import (
    script as subroutine_0x357604,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X357604,
    start=0x357604,
    end=0x3576B7,
    scripts=[
        subroutine_0x357604,
    ],
)

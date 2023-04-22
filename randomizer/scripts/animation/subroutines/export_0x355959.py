# pylint: disable=C0301,C0103

"""exports subroutine 0X355959"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X355959,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x355959 import (
    script as subroutine_0x355959,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X355959,
    start=0x355959,
    end=0x3559EF,
    scripts=[
        subroutine_0x355959,
    ],
)

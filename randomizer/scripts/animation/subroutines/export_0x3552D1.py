# pylint: disable=C0301,C0103

"""exports subroutine 0X3552D1"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3552D1,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3552D1 import (
    script as subroutine_0x3552D1,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3552D1,
    start=0x3552D1,
    end=0x355498,
    scripts=[
        subroutine_0x3552D1,
    ],
)

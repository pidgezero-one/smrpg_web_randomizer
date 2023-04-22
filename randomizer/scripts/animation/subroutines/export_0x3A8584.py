# pylint: disable=C0301,C0103

"""exports subroutine 0X3A8584"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A8584,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A8584 import (
    script as subroutine_0x3A8584,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A8584,
    start=0x3A8584,
    end=0x3A858D,
    scripts=[
        subroutine_0x3A8584,
    ],
)

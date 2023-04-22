# pylint: disable=C0301,C0103

"""exports subroutine 0X3A7D04"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A7D04,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A7D04 import (
    script as subroutine_0x3A7D04,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A7D04,
    start=0x3A7D04,
    end=0x3A7D0C,
    scripts=[
        subroutine_0x3A7D04,
    ],
)

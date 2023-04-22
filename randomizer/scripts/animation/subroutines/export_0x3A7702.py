# pylint: disable=C0301,C0103

"""exports subroutine 0X3A7702"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A7702,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A7702 import (
    script as subroutine_0x3A7702,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A7702,
    start=0x3A7702,
    end=0x3A785C,
    scripts=[
        subroutine_0x3A7702,
    ],
)

# pylint: disable=C0301,C0103

"""exports subroutine 0X350606"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X350606,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x350606 import (
    script as subroutine_0x350606,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X350606,
    start=0x350606,
    end=0x350606,
    scripts=[
        subroutine_0x350606,
    ],
)

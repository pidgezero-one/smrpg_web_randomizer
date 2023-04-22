# pylint: disable=C0301,C0103

"""exports subroutine 0X3593A3"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3593A3,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3593A3 import (
    script as subroutine_0x3593A3,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3593A3,
    start=0x3593A3,
    end=0x3595C0,
    scripts=[
        subroutine_0x3593A3,
    ],
)

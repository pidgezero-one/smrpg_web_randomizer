# pylint: disable=C0301,C0103

"""exports subroutine 0X3A7A03"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A7A03,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A7A03 import (
    script as subroutine_0x3A7A03,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A7A03,
    start=0x3A7A03,
    end=0x3A7A14,
    scripts=[
        subroutine_0x3A7A03,
    ],
)

# pylint: disable=C0301,C0103

"""exports subroutine 0X3AC148"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3AC148,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3AC148 import (
    script as subroutine_0x3AC148,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3AC148,
    start=0x3AC148,
    end=0x3AC1EF,
    scripts=[
        subroutine_0x3AC148,
    ],
)

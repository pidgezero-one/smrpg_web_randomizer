# pylint: disable=C0301,C0103

"""exports subroutine 0X3578F1"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3578F1,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3578F1 import (
    script as subroutine_0x3578F1,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3578F1,
    start=0x3578F1,
    end=0x35791C,
    scripts=[
        subroutine_0x3578F1,
    ],
)

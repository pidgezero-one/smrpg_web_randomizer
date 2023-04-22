# pylint: disable=C0301,C0103

"""exports subroutine 0X3551FE"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3551FE,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3551FE import (
    script as subroutine_0x3551FE,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3551FE,
    start=0x3551FE,
    end=0x355233,
    scripts=[
        subroutine_0x3551FE,
    ],
)

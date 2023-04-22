# pylint: disable=C0301,C0103

"""exports subroutine 0X3A8A7E"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A8A7E,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A8A7E import (
    script as subroutine_0x3A8A7E,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A8A7E,
    start=0x3A8A7E,
    end=0x3A8ABF,
    scripts=[
        subroutine_0x3A8A7E,
    ],
)

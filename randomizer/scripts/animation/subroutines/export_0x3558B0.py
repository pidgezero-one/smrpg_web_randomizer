# pylint: disable=C0301,C0103

"""exports subroutine 0X3558B0"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3558B0,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3558B0 import (
    script as subroutine_0x3558B0,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3558B0,
    start=0x3558B0,
    end=0x355950,
    scripts=[
        subroutine_0x3558B0,
    ],
)

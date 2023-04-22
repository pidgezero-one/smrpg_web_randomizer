# pylint: disable=C0301,C0103

"""exports subroutine 0X354900"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X354900,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x354900 import (
    script as subroutine_0x354900,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X354900,
    start=0x354900,
    end=0x354914,
    scripts=[
        subroutine_0x354900,
    ],
)

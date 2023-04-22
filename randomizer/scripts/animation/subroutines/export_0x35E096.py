# pylint: disable=C0301,C0103

"""exports subroutine 0X35E096"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35E096,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35E096 import (
    script as subroutine_0x35E096,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35E096,
    start=0x35E096,
    end=0x35E5D7,
    scripts=[
        subroutine_0x35E096,
    ],
)

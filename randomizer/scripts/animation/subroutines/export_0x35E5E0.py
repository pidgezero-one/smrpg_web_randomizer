# pylint: disable=C0301,C0103

"""exports subroutine 0X35E5E0"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35E5E0,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35E5E0 import (
    script as subroutine_0x35E5E0,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35E5E0,
    start=0x35E5E0,
    end=0x35E758,
    scripts=[
        subroutine_0x35E5E0,
    ],
)

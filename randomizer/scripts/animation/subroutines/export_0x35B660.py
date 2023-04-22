# pylint: disable=C0301,C0103

"""exports subroutine 0X35B660"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35B660,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35B660 import (
    script as subroutine_0x35B660,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35B660,
    start=0x35B660,
    end=0x35B944,
    scripts=[
        subroutine_0x35B660,
    ],
)

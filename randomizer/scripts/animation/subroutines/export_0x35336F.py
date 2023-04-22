# pylint: disable=C0301,C0103

"""exports subroutine 0X35336F"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35336F,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35336F import (
    script as subroutine_0x35336F,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35336F,
    start=0x35336F,
    end=0x35342B,
    scripts=[
        subroutine_0x35336F,
    ],
)

# pylint: disable=C0301,C0103

"""exports subroutine 0X35DCE9"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35DCE9,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35DCE9 import (
    script as subroutine_0x35DCE9,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35DCE9,
    start=0x35DCE9,
    end=0x35DCFC,
    scripts=[
        subroutine_0x35DCE9,
    ],
)

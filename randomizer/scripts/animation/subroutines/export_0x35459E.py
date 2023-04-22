# pylint: disable=C0301,C0103

"""exports subroutine 0X35459E"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35459E,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35459E import (
    script as subroutine_0x35459E,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35459E,
    start=0x35459E,
    end=0x3547C1,
    scripts=[
        subroutine_0x35459E,
    ],
)

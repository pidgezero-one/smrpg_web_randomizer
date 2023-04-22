# pylint: disable=C0301,C0103

"""exports subroutine 0X3A7A93"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A7A93,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A7A93 import (
    script as subroutine_0x3A7A93,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A7A93,
    start=0x3A7A93,
    end=0x3A7A9B,
    scripts=[
        subroutine_0x3A7A93,
    ],
)

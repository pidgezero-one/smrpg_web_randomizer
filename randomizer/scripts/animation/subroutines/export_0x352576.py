# pylint: disable=C0301,C0103

"""exports subroutine 0X352576"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X352576,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x352576 import (
    script as subroutine_0x352576,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X352576,
    start=0x352576,
    end=0x3525A2,
    scripts=[
        subroutine_0x352576,
    ],
)

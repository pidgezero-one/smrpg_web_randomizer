# pylint: disable=C0301,C0103

"""exports subroutine 0X35DB5D"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35DB5D,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35DB5D import (
    script as subroutine_0x35DB5D,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35DB5D,
    start=0x35DB5D,
    end=0x35DC6B,
    scripts=[
        subroutine_0x35DB5D,
    ],
)

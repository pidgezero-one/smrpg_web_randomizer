# pylint: disable=C0301,C0103

"""exports subroutine 0X35F732"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35F732,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35F732 import (
    script as subroutine_0x35F732,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F732,
    start=0x35F732,
    end=0x35F782,
    scripts=[
        subroutine_0x35F732,
    ],
)

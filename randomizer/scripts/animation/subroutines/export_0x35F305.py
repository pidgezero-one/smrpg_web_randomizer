# pylint: disable=C0301,C0103

"""exports subroutine 0X35F305"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35F305,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35F305 import (
    script as subroutine_0x35F305,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F305,
    start=0x35F305,
    end=0x35F35E,
    scripts=[
        subroutine_0x35F305,
    ],
)

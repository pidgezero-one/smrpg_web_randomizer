# pylint: disable=C0301,C0103

"""exports subroutine 0X35FC8F"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35FC8F,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35FC8F import (
    script as subroutine_0x35FC8F,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35FC8F,
    start=0x35FC8F,
    end=0x35FD47,
    scripts=[
        subroutine_0x35FC8F,
    ],
)

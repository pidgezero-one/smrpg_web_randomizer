# pylint: disable=C0301,C0103

"""exports subroutine 0X35FD9A"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35FD9A,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35FD9A import (
    script as subroutine_0x35FD9A,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35FD9A,
    start=0x35FD9A,
    end=0x35FEEA,
    scripts=[
        subroutine_0x35FD9A,
    ],
)

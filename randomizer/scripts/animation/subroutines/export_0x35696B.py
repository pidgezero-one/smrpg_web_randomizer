# pylint: disable=C0301,C0103

"""exports subroutine 0X35696B"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35696B,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35696B import (
    script as subroutine_0x35696B,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35696B,
    start=0x35696B,
    end=0x3569A9,
    scripts=[
        subroutine_0x35696B,
    ],
)

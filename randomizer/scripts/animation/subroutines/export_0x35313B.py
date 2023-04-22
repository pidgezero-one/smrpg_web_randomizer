# pylint: disable=C0301,C0103

"""exports subroutine 0X35313B"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35313B,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35313B import (
    script as subroutine_0x35313B,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35313B,
    start=0x35313B,
    end=0x3531ED,
    scripts=[
        subroutine_0x35313B,
    ],
)

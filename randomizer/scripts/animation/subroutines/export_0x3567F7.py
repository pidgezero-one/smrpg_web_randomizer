# pylint: disable=C0301,C0103

"""exports subroutine 0X3567F7"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3567F7,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3567F7 import (
    script as subroutine_0x3567F7,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3567F7,
    start=0x3567F7,
    end=0x35682A,
    scripts=[
        subroutine_0x3567F7,
    ],
)

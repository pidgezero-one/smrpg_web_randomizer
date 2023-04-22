# pylint: disable=C0301,C0103

"""exports subroutine 0X3542DD"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3542DD,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3542DD import (
    script as subroutine_0x3542DD,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3542DD,
    start=0x3542DD,
    end=0x3542FF,
    scripts=[
        subroutine_0x3542DD,
    ],
)

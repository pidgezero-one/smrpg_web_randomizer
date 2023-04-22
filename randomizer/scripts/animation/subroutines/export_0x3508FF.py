# pylint: disable=C0301,C0103

"""exports subroutine 0X3508FF"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3508FF,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3508FF import (
    script as subroutine_0x3508FF,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3508FF,
    start=0x3508FF,
    end=0x350915,
    scripts=[
        subroutine_0x3508FF,
    ],
)

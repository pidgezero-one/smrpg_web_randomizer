# pylint: disable=C0301,C0103

"""exports subroutine 0X353F81"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X353F81,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x353F81 import (
    script as subroutine_0x353F81,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X353F81,
    start=0x353F81,
    end=0x3540AF,
    scripts=[
        subroutine_0x353F81,
    ],
)

# pylint: disable=C0301,C0103

"""exports subroutine 0X353DDA"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X353DDA,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x353DDA import (
    script as subroutine_0x353DDA,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X353DDA,
    start=0x353DDA,
    end=0x353F10,
    scripts=[
        subroutine_0x353DDA,
    ],
)

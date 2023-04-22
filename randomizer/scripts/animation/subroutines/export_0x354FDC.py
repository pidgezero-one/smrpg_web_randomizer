# pylint: disable=C0301,C0103

"""exports subroutine 0X354FDC"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X354FDC,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x354FDC import (
    script as subroutine_0x354FDC,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X354FDC,
    start=0x354FDC,
    end=0x3551CA,
    scripts=[
        subroutine_0x354FDC,
    ],
)

# pylint: disable=C0301,C0103

"""exports subroutine 0X35BE0E"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35BE0E,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35BE0E import (
    script as subroutine_0x35BE0E,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35BE0E,
    start=0x35BE0E,
    end=0x35BEAF,
    scripts=[
        subroutine_0x35BE0E,
    ],
)

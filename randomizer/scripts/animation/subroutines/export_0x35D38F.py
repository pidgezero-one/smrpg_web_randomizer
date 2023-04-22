# pylint: disable=C0301,C0103

"""exports subroutine 0X35D38F"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35D38F,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35D38F import (
    script as subroutine_0x35D38F,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35D38F,
    start=0x35D38F,
    end=0x35D45C,
    scripts=[
        subroutine_0x35D38F,
    ],
)

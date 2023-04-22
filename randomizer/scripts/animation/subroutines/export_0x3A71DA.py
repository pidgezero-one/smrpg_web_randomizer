# pylint: disable=C0301,C0103

"""exports subroutine 0X3A71DA"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A71DA,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A71DA import (
    script as subroutine_0x3A71DA,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A71DA,
    start=0x3A71DA,
    end=0x3A72B5,
    scripts=[
        subroutine_0x3A71DA,
    ],
)

# pylint: disable=C0301,C0103

"""exports subroutine 0X35AD5C"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35AD5C,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35AD5C import (
    script as subroutine_0x35AD5C,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35AD5C,
    start=0x35AD5C,
    end=0x35B019,
    scripts=[
        subroutine_0x35AD5C,
    ],
)

# pylint: disable=C0301,C0103

"""exports subroutine 0X02F50E"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X02F50E,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x02F50E import (
    script as subroutine_0x02F50E,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X02F50E,
    start=0x02F50E,
    end=0x02F51D,
    scripts=[
        subroutine_0x02F50E,
    ],
)

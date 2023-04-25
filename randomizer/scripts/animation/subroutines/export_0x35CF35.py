# pylint: disable=C0301,C0103

"""exports subroutine 0X35CF35"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35CF35,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35CF35 import (
    script as subroutine_0x35CF35,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35CF35,
    start=0x35CF35,
    end=0x35D186,
    scripts=[
        subroutine_0x35CF35,
    ],
)

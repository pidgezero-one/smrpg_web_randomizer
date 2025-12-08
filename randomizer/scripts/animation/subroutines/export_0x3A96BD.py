# pylint: disable=C0301,C0103

"""exports subroutine 0X3A96BD"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3A96BD)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A96BD import (
    script as subroutine_0x3A96BD)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A96BD,
    start=0x3A96BD,
    end=0x3A971C,
    scripts=[
        subroutine_0x3A96BD,
    ])

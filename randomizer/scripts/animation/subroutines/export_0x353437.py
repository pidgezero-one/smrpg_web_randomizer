# pylint: disable=C0301,C0103

"""exports subroutine 0X353437"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X353437)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x353437 import (
    script as subroutine_0x353437)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X353437,
    start=0x353437,
    end=0x353705,
    scripts=[
        subroutine_0x353437,
    ])

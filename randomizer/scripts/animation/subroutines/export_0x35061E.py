# pylint: disable=C0301,C0103

"""exports subroutine 0X35061E"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35061E)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35061E import (
    script as subroutine_0x35061E)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35061E,
    start=0x35061E,
    end=0x3506FF,
    scripts=[
        subroutine_0x35061E,
    ])

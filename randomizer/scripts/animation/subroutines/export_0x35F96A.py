# pylint: disable=C0301,C0103

"""exports subroutine 0X35F96A"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35F96A)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35F96A import (
    script as subroutine_0x35F96A)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F96A,
    start=0x35F96A,
    end=0x35F9A1,
    scripts=[
        subroutine_0x35F96A,
    ])

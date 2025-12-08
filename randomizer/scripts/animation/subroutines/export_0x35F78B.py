# pylint: disable=C0301,C0103

"""exports subroutine 0X35F78B"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35F78B)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35F78B import (
    script as subroutine_0x35F78B)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F78B,
    start=0x35F78B,
    end=0x35F816,
    scripts=[
        subroutine_0x35F78B,
    ])

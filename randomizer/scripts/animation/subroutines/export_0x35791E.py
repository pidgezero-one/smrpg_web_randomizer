# pylint: disable=C0301,C0103

"""exports subroutine 0X35791E"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35791E)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35791E import (
    script as subroutine_0x35791E)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35791E,
    start=0x35791E,
    end=0x35794F,
    scripts=[
        subroutine_0x35791E,
    ])

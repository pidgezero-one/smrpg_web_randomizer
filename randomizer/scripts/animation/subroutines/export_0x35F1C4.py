# pylint: disable=C0301,C0103

"""exports subroutine 0X35F1C4"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35F1C4)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35F1C4 import (
    script as subroutine_0x35F1C4)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F1C4,
    start=0x35F1C4,
    end=0x35F214,
    scripts=[
        subroutine_0x35F1C4,
    ])

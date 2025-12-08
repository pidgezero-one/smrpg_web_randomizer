# pylint: disable=C0301,C0103

"""exports subroutine 0X35D191"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35D191)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35D191 import (
    script as subroutine_0x35D191)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35D191,
    start=0x35D191,
    end=0x35D1FD,
    scripts=[
        subroutine_0x35D191,
    ])

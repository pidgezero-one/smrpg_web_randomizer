# pylint: disable=C0301,C0103

"""exports subroutine 0X35DAE3"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35DAE3)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35DAE3 import (
    script as subroutine_0x35DAE3)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35DAE3,
    start=0x35DAE3,
    end=0x35DB50,
    scripts=[
        subroutine_0x35DAE3,
    ])

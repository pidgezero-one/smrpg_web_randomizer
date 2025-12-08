# pylint: disable=C0301,C0103

"""exports subroutine 0X3A82AA"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3A82AA)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A82AA import (
    script as subroutine_0x3A82AA)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A82AA,
    start=0x3A82AA,
    end=0x3A82C7,
    scripts=[
        subroutine_0x3A82AA,
    ])

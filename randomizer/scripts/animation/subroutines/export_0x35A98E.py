# pylint: disable=C0301,C0103

"""exports subroutine 0X35A98E"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X35A98E)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35A98E import (
    script as subroutine_0x35A98E)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35A98E,
    start=0x35A98E,
    end=0x35ABAC,
    scripts=[
        subroutine_0x35A98E,
    ])

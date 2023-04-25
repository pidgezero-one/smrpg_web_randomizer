# pylint: disable=C0301,C0103

"""exports subroutine 0X3540CA"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X3540CA,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3540CA import (
    script as subroutine_0x3540CA,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3540CA,
    start=0x3540CA,
    end=0x3542BE,
    scripts=[
        subroutine_0x3540CA,
    ],
)

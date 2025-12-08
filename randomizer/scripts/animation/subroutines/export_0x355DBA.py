# pylint: disable=C0301,C0103

"""exports subroutine 0X355DBA"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    SUBROUTINES_0X355DBA)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x355DBA import (
    script as subroutine_0x355DBA)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X355DBA,
    start=0x355DBA,
    end=0x355E00,
    scripts=[
        subroutine_0x355DBA,
    ])

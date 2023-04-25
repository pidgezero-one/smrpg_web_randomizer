"""behaviour 12 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_12_0X3508A4,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_12 import (
    script as subroutine_0x12,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_12_0X3508A4,
    start=0x3508A4,
    end=0x3508B9,
    scripts=[
        subroutine_0x12,
    ],
)

"""behaviour 40 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_40_0X350DA3,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_40 import (
    script as subroutine_0x40,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_40_0X350DA3,
    start=0x350DA3,
    end=0x350DAE,
    scripts=[
        subroutine_0x40,
    ],
)

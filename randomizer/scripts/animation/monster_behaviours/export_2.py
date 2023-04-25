"""behaviour 2 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_2_0X350635,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_2 import (
    script as subroutine_0x2,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_2_0X350635,
    start=0x350635,
    end=0x350668,
    scripts=[
        subroutine_0x2,
    ],
)

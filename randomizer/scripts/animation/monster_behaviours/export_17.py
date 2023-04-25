"""behaviour 17 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_17_0X35096F,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_17 import (
    script as subroutine_0x17,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_17_0X35096F,
    start=0x35096F,
    end=0x3508B7,
    scripts=[
        subroutine_0x17,
    ],
)

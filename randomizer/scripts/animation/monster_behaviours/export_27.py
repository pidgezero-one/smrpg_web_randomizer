"""behaviour 27 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_27_0X350B2D,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_27 import (
    script as subroutine_0x27,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_27_0X350B2D,
    start=0x350B2D,
    end=0x350B7F,
    scripts=[
        subroutine_0x27,
    ],
)

"""behaviour 3 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_3_0X350669)
from randomizer.scripts.animation.monster_behaviours.contents.script_3 import (
    script as subroutine_0x3)

bank = AnimationScriptBank(
    name=BEHAVIOUR_3_0X350669,
    start=0x350669,
    end=0x3506A6,
    scripts=[
        subroutine_0x3,
    ])

"""behaviour 30 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_30_0X350BF9)
from randomizer.scripts.animation.monster_behaviours.contents.script_30 import (
    script as subroutine_0x30)

bank = AnimationScriptBank(
    name=BEHAVIOUR_30_0X350BF9,
    start=0x350BF9,
    end=0x350BFC,
    scripts=[
        subroutine_0x30,
    ])

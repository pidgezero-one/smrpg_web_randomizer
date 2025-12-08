"""behaviour 33 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_33_0X350C5B)
from randomizer.scripts.animation.monster_behaviours.contents.script_33 import (
    script as subroutine_0x33)

bank = AnimationScriptBank(
    name=BEHAVIOUR_33_0X350C5B,
    start=0x350C5B,
    end=0x350C9D,
    scripts=[
        subroutine_0x33,
    ])

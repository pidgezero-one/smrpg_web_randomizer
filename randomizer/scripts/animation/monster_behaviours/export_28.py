"""behaviour 28 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_28_0X350BB7)
from randomizer.scripts.animation.monster_behaviours.contents.script_28 import (
    script as subroutine_0x28)

bank = AnimationScriptBank(
    name=BEHAVIOUR_28_0X350BB7,
    start=0x350BB7,
    end=0x350BF2,
    scripts=[
        subroutine_0x28,
    ])

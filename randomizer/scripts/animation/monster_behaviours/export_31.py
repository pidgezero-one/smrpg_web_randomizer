"""behaviour 31 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_31_0X350BFD,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_31 import (
    script as subroutine_0x31,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_31_0X350BFD,
    start=0x350BFD,
    end=0x350C0D,
    scripts=[
        subroutine_0x31,
    ],
)

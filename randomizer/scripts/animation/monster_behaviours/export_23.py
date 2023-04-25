"""behaviour 23 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_23_0X350A55,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_23 import (
    script as subroutine_0x23,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_23_0X350A55,
    start=0x350A55,
    end=0x350A9B,
    scripts=[
        subroutine_0x23,
    ],
)

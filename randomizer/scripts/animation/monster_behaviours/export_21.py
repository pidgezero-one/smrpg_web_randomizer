"""behaviour 21 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_21_0X350A38,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_21 import (
    script as subroutine_0x21,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_21_0X350A38,
    start=0x350A38,
    end=0x350A3D,
    scripts=[
        subroutine_0x21,
    ],
)

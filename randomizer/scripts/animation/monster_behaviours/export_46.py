"""behaviour 46 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_46_0X350E98,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_46 import (
    script as subroutine_0x46,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_46_0X350E98,
    start=0x350E98,
    end=0x350ED0,
    scripts=[
        subroutine_0x46,
    ],
)

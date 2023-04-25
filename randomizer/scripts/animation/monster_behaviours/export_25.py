"""behaviour 25 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_25_0X350ABD,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_25 import (
    script as subroutine_0x25,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_25_0X350ABD,
    start=0x350ABD,
    end=0x350AD2,
    scripts=[
        subroutine_0x25,
    ],
)

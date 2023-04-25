"""behaviour 35 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_35_0X350CDC,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_35 import (
    script as subroutine_0x35,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_35_0X350CDC,
    start=0x350CDC,
    end=0x350CF1,
    scripts=[
        subroutine_0x35,
    ],
)

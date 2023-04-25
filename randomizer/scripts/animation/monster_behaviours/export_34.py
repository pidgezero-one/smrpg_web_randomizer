"""behaviour 34 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_34_0X350C9E,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_34 import (
    script as subroutine_0x34,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_34_0X350C9E,
    start=0x350C9E,
    end=0x350CDB,
    scripts=[
        subroutine_0x34,
    ],
)

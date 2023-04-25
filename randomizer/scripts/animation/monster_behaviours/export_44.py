"""behaviour 44 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_44_0X350E4A,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_44 import (
    script as subroutine_0x44,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_44_0X350E4A,
    start=0x350E4A,
    end=0x350E5F,
    scripts=[
        subroutine_0x44,
    ],
)

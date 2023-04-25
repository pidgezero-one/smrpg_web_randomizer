"""behaviour 45 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_45_0X350E84,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_45 import (
    script as subroutine_0x45,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_45_0X350E84,
    start=0x350E84,
    end=0x350E97,
    scripts=[
        subroutine_0x45,
    ],
)

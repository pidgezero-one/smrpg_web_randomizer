"""behaviour 43 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_43_0X350E38)
from randomizer.scripts.animation.monster_behaviours.contents.script_43 import (
    script as subroutine_0x43)

bank = AnimationScriptBank(
    name=BEHAVIOUR_43_0X350E38,
    start=0x350E38,
    end=0x350E49,
    scripts=[
        subroutine_0x43,
    ])

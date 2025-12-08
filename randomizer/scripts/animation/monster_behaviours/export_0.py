"""behaviour 0 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_0_0X3505C6)
from randomizer.scripts.animation.monster_behaviours.contents.script_0 import (
    script as subroutine_0x0)

bank = AnimationScriptBank(
    name=BEHAVIOUR_0_0X3505C6,
    start=0x3505C6,
    end=0x3505D9,
    scripts=[
        subroutine_0x0,
    ])

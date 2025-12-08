"""behaviour 9 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_9_0X3507E9)
from randomizer.scripts.animation.monster_behaviours.contents.script_9 import (
    script as subroutine_0x9)

bank = AnimationScriptBank(
    name=BEHAVIOUR_9_0X3507E9,
    start=0x3507E9,
    end=0x35082F,
    scripts=[
        subroutine_0x9,
    ])

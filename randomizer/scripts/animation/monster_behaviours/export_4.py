"""behaviour 4 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_4_0X3506A7)
from randomizer.scripts.animation.monster_behaviours.contents.script_4 import (
    script as subroutine_0x4)

bank = AnimationScriptBank(
    name=BEHAVIOUR_4_0X3506A7,
    start=0x3506A7,
    end=0x3506FF,
    scripts=[
        subroutine_0x4,
    ])

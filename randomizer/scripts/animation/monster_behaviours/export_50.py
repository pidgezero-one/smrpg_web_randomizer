"""behaviour 50 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_50_0X350F4A)
from randomizer.scripts.animation.monster_behaviours.contents.script_50 import (
    script as subroutine_0x50)

bank = AnimationScriptBank(
    name=BEHAVIOUR_50_0X350F4A,
    start=0x350F4A,
    end=0x350F55,
    scripts=[
        subroutine_0x50,
    ])

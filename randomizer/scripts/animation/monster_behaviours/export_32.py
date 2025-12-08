"""behaviour 32 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_32_0X350C14)
from randomizer.scripts.animation.monster_behaviours.contents.script_32 import (
    script as subroutine_0x32)

bank = AnimationScriptBank(
    name=BEHAVIOUR_32_0X350C14,
    start=0x350C14,
    end=0x350C5A,
    scripts=[
        subroutine_0x32,
    ])

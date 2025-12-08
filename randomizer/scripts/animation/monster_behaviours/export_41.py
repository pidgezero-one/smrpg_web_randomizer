"""behaviour 41 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_41_0X350DAF)
from randomizer.scripts.animation.monster_behaviours.contents.script_41 import (
    script as subroutine_0x41)

bank = AnimationScriptBank(
    name=BEHAVIOUR_41_0X350DAF,
    start=0x350DAF,
    end=0x350DEC,
    scripts=[
        subroutine_0x41,
    ])

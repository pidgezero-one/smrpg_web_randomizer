"""behaviour 22 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_22_0X350A3E)
from randomizer.scripts.animation.monster_behaviours.contents.script_22 import (
    script as subroutine_0x22)

bank = AnimationScriptBank(
    name=BEHAVIOUR_22_0X350A3E,
    start=0x350A3E,
    end=0x350A4E,
    scripts=[
        subroutine_0x22,
    ])

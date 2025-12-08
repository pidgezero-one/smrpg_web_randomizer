"""behaviour 18 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_18_0X35099D)
from randomizer.scripts.animation.monster_behaviours.contents.script_18 import (
    script as subroutine_0x18)

bank = AnimationScriptBank(
    name=BEHAVIOUR_18_0X35099D,
    start=0x35099D,
    end=0x3509D4,
    scripts=[
        subroutine_0x18,
    ])

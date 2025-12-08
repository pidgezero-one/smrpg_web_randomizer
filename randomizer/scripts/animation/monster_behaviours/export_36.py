"""behaviour 36 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_36_0X350D22)
from randomizer.scripts.animation.monster_behaviours.contents.script_36 import (
    script as subroutine_0x36)

bank = AnimationScriptBank(
    name=BEHAVIOUR_36_0X350D22,
    start=0x350D22,
    end=0x350D35,
    scripts=[
        subroutine_0x36,
    ])

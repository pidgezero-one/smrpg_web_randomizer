"""behaviour 38 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_38_0X350D72)
from randomizer.scripts.animation.monster_behaviours.contents.script_38 import (
    script as subroutine_0x38)

bank = AnimationScriptBank(
    name=BEHAVIOUR_38_0X350D72,
    start=0x350D72,
    end=0x350D9C,
    scripts=[
        subroutine_0x38,
    ])

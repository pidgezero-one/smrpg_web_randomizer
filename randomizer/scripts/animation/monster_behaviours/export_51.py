"""behaviour 51 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_51_0X350F56)
from randomizer.scripts.animation.monster_behaviours.contents.script_51 import (
    script as subroutine_0x51)

bank = AnimationScriptBank(
    name=BEHAVIOUR_51_0X350F56,
    start=0x350F56,
    end=0x350F6A,
    scripts=[
        subroutine_0x51,
    ])

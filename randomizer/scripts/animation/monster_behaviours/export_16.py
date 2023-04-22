"""behaviour 16 export"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_16_0X350928,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_16 import (
    script as subroutine_0x16,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_16_0X350928,
    start=0x350928,
    end=0x35096E,
    scripts=[
        subroutine_0x16,
    ],
)

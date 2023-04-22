"""behaviour 8 export"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_8_0X3507A2,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_8 import (
    script as subroutine_0x8,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_8_0X3507A2,
    start=0x3507A2,
    end=0x3507E8,
    scripts=[
        subroutine_0x8,
    ],
)

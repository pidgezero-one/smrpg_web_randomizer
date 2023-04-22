"""behaviour 1 export"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_1_0X3505DA,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_1 import (
    script as subroutine_0x1,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_1_0X3505DA,
    start=0x3505DA,
    end=0x3505FD,
    scripts=[
        subroutine_0x1,
    ],
)

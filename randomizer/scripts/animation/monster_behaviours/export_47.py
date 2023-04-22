"""behaviour 47 export"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_47_0X350EEE,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_47 import (
    script as subroutine_0x47,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_47_0X350EEE,
    start=0x350EEE,
    end=0x350F19,
    scripts=[
        subroutine_0x47,
    ],
)

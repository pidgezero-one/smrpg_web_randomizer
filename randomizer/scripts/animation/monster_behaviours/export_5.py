"""behaviour 5 export"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_5_0X350737,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_5 import (
    script as subroutine_0x5,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_5_0X350737,
    start=0x350737,
    end=0x350758,
    scripts=[
        subroutine_0x5,
    ],
)

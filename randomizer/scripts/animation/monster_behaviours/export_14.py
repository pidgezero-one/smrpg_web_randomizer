"""behaviour 14 export"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_14_0X350916,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_14 import (
    script as subroutine_0x14,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_14_0X350916,
    start=0x350916,
    end=0x35091B,
    scripts=[
        subroutine_0x14,
    ],
)

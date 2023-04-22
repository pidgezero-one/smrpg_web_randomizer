"""behaviour 48 export"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_48_0X350F1A,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_48 import (
    script as subroutine_0x48,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_48_0X350F1A,
    start=0x350F1A,
    end=0x350F43,
    scripts=[
        subroutine_0x48,
    ],
)

"""behaviour 49 export"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_49_0X350F44,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_49 import (
    script as subroutine_0x49,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_49_0X350F44,
    start=0x350F44,
    end=0x350F49,
    scripts=[
        subroutine_0x49,
    ],
)

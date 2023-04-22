"""behaviour 10 export"""

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_10_0X350830,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_10 import (
    script as subroutine_0x10,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_10_0X350830,
    start=0x350830,
    end=0x350869,
    scripts=[
        subroutine_0x10,
    ],
)

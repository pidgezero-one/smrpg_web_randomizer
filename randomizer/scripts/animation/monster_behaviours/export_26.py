"""behaviour 26 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_26_0X350AF7,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_26 import (
    script as subroutine_0x26,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_26_0X350AF7,
    start=0x350AF7,
    end=0x350B2C,
    scripts=[
        subroutine_0x26,
    ],
)

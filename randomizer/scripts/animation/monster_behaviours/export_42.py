"""behaviour 42 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_42_0X350DED,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_42 import (
    script as subroutine_0x42,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_42_0X350DED,
    start=0x350DED,
    end=0x350E37,
    scripts=[
        subroutine_0x42,
    ],
)

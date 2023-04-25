"""behaviour 11 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_11_0X35086A,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_11 import (
    script as subroutine_0x11,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_11_0X35086A,
    start=0x35086A,
    end=0x350897,
    scripts=[
        subroutine_0x11,
    ],
)

"""behaviour 20 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_20_0X3509D5,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_20 import (
    script as subroutine_0x20,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_20_0X3509D5,
    start=0x3509D5,
    end=0x350A00,
    scripts=[
        subroutine_0x20,
    ],
)

"""behaviour 37 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_37_0X350D36,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_37 import (
    script as subroutine_0x37,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_37_0X350D36,
    start=0x350D36,
    end=0x350D71,
    scripts=[
        subroutine_0x37,
    ],
)

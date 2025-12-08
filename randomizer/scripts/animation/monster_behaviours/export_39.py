"""behaviour 39 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_39_0X350D9D)
from randomizer.scripts.animation.monster_behaviours.contents.script_39 import (
    script as subroutine_0x39)

bank = AnimationScriptBank(
    name=BEHAVIOUR_39_0X350D9D,
    start=0x350D9D,
    end=0x350DA2,
    scripts=[
        subroutine_0x39,
    ])

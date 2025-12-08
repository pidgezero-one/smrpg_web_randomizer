"""behaviour 24 export"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    BEHAVIOUR_24_0X350A9C)
from randomizer.scripts.animation.monster_behaviours.contents.script_24 import (
    script as subroutine_0x24)

bank = AnimationScriptBank(
    name=BEHAVIOUR_24_0X350A9C,
    start=0x350A9C,
    end=0x350ABC,
    scripts=[
        subroutine_0x24,
    ])

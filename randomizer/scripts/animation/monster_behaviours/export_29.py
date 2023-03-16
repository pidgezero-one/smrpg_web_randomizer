from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_29_0X350BF3,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_29 import (
    script as subroutine_0x29,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_29_0X350BF3,
    start=0x350BF3,
    end=0x350BF8,
    scripts=[
        subroutine_0x29,
    ],
)

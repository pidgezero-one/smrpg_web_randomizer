from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_50_0X350F4A,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_50 import (
    script as subroutine_0x50,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_50_0X350F4A,
    start=0x350F4A,
    end=0x350F55,
    scripts=[
        subroutine_0x50,
    ],
)

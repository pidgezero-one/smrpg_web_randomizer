from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_52_0X350F6B,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_52 import (
    script as subroutine_0x52,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_52_0X350F6B,
    start=0x350F6B,
    end=0x350F79,
    scripts=[
        subroutine_0x52,
    ],
)

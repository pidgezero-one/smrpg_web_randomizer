from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_53_0X350F7A,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_53 import (
    script as subroutine_0x53,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_53_0X350F7A,
    start=0x350F7A,
    end=0x351025,
    scripts=[
        subroutine_0x53,
    ],
)

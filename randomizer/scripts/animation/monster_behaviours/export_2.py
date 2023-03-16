from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_2_0X350635,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_2 import (
    script as subroutine_0x2,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_2_0X350635,
    start=0x350635,
    end=0x350668,
    scripts=[
        subroutine_0x2,
    ],
)

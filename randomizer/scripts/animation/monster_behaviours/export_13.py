from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_13_0X3508BA,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_13 import (
    script as subroutine_0x13,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_13_0X3508BA,
    start=0x3508BA,
    end=0x3508DE,
    scripts=[
        subroutine_0x13,
    ],
)

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_26_0X350AF7,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_26 import (
    script as subroutine_0x26,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_26_0X350AF7,
    start=0x350AF7,
    end=0x350B2C,
    scripts=[
        subroutine_0x26,
    ],
)

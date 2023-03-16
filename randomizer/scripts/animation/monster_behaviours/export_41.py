from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_41_0X350DAF,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_41 import (
    script as subroutine_0x41,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_41_0X350DAF,
    start=0x350DAF,
    end=0x350DEC,
    scripts=[
        subroutine_0x41,
    ],
)

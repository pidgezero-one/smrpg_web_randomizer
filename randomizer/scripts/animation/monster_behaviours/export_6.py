from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_6_0X350790,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_6 import (
    script as subroutine_0x6,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_6_0X350790,
    start=0x350790,
    end=0x350795,
    scripts=[
        subroutine_0x6,
    ],
)

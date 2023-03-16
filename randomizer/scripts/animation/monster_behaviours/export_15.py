from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_15_0X35091C,
)
from randomizer.scripts.animation.monster_behaviours.contents.script_15 import (
    script as subroutine_0x15,
)

bank = AnimationScriptBank(
    name=BEHAVIOUR_15_0X35091C,
    start=0x35091C,
    end=0x350927,
    scripts=[
        subroutine_0x15,
    ],
)

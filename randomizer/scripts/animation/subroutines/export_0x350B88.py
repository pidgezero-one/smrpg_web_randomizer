from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X350B88,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x350B88 import (
    script as subroutine_0x350B88,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X350B88,
    start=0x350B88,
    end=0x350B88,
    scripts=[
        subroutine_0x350B88,
    ],
)

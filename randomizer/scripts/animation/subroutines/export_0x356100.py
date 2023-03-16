from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X356100,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x356100 import (
    script as subroutine_0x356100,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356100,
    start=0x356100,
    end=0x356130,
    scripts=[
        subroutine_0x356100,
    ],
)

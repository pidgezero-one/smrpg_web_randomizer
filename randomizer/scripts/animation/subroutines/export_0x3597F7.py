from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3597F7,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3597F7 import (
    script as subroutine_0x3597F7,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3597F7,
    start=0x3597F7,
    end=0x3599E5,
    scripts=[
        subroutine_0x3597F7,
    ],
)

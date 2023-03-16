from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3547FA,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3547FA import (
    script as subroutine_0x3547FA,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3547FA,
    start=0x3547FA,
    end=0x354891,
    scripts=[
        subroutine_0x3547FA,
    ],
)

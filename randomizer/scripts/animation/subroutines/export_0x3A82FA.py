from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A82FA,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A82FA import (
    script as subroutine_0x3A82FA,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A82FA,
    start=0x3A82FA,
    end=0x3A8303,
    scripts=[
        subroutine_0x3A82FA,
    ],
)

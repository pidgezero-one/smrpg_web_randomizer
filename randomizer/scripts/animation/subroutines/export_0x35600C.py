from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35600C,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35600C import (
    script as subroutine_0x35600C,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35600C,
    start=0x35600C,
    end=0x356040,
    scripts=[
        subroutine_0x35600C,
    ],
)

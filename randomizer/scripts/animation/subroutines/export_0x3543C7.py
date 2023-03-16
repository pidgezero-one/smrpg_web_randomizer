from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3543C7,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3543C7 import (
    script as subroutine_0x3543C7,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3543C7,
    start=0x3543C7,
    end=0x35458B,
    scripts=[
        subroutine_0x3543C7,
    ],
)

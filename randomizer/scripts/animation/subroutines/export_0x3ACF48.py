from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3ACF48,
)
from .contents.subroutine_0x3ACF48 import script as subroutine_0x3ACF48

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3ACF48,
    start=0x3ACF48,
    end=0x3AD6F3,
    scripts=[
        subroutine_0x3ACF48,
    ],
)

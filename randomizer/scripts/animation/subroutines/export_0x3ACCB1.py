from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3ACCB1,
)
from .contents.subroutine_0x3ACCB1 import script as subroutine_0x3ACCB1

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3ACCB1,
    start=0x3ACCB1,
    end=0x3ACF43,
    scripts=[
        subroutine_0x3ACCB1,
    ],
)

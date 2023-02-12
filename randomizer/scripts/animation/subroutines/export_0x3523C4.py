from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3523C4,
)
from .contents.subroutine_0x3523C4 import script as subroutine_0x3523C4

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3523C4,
    start=0x3523C4,
    end=0x3523FC,
    scripts=[
        subroutine_0x3523C4,
    ],
)

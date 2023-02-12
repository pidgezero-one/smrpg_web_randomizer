from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X354B35,
)
from .contents.subroutine_0x354B35 import script as subroutine_0x354B35

bank = AnimationScriptBank(
    name=SUBROUTINES_0X354B35,
    start=0x354B35,
    end=0x354BB3,
    scripts=[
        subroutine_0x354B35,
    ],
)

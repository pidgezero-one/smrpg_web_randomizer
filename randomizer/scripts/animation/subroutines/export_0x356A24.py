from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X356A24,
)
from .contents.subroutine_0x356A24 import script as subroutine_0x356A24

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356A24,
    start=0x356A24,
    end=0x356A7D,
    scripts=[
        subroutine_0x356A24,
    ],
)

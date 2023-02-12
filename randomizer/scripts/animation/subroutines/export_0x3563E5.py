from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3563E5,
)
from .contents.subroutine_0x3563E5 import script as subroutine_0x3563E5

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3563E5,
    start=0x3563E5,
    end=0x356455,
    scripts=[
        subroutine_0x3563E5,
    ],
)

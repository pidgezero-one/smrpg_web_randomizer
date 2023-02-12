from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X357AE5,
)
from .contents.subroutine_0x357AE5 import script as subroutine_0x357AE5

bank = AnimationScriptBank(
    name=SUBROUTINES_0X357AE5,
    start=0x357AE5,
    end=0x357B71,
    scripts=[
        subroutine_0x357AE5,
    ],
)

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35B038,
)
from .contents.subroutine_0x35B038 import script as subroutine_0x35B038

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35B038,
    start=0x35B038,
    end=0x35B35C,
    scripts=[
        subroutine_0x35B038,
    ],
)

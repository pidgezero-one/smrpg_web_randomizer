from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35F4AF,
)
from .contents.subroutine_0x35F4AF import script as subroutine_0x35F4AF

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F4AF,
    start=0x35F4AF,
    end=0x35F541,
    scripts=[
        subroutine_0x35F4AF,
    ],
)

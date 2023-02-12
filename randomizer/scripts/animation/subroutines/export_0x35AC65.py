from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35AC65,
)
from .contents.subroutine_0x35AC65 import script as subroutine_0x35AC65

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35AC65,
    start=0x35AC65,
    end=0x35AD49,
    scripts=[
        subroutine_0x35AC65,
    ],
)

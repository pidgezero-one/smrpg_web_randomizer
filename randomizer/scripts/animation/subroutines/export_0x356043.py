from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X356043,
)
from .contents.subroutine_0x356043 import script as subroutine_0x356043

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356043,
    start=0x356043,
    end=0x35605E,
    scripts=[
        subroutine_0x356043,
    ],
)

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35E049,
)
from .contents.subroutine_0x35E049 import script as subroutine_0x35E049

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35E049,
    start=0x35E049,
    end=0x35E07B,
    scripts=[
        subroutine_0x35E049,
    ],
)

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A7999,
)
from .contents.subroutine_0x3A7999 import script as subroutine_0x3A7999

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A7999,
    start=0x3A7999,
    end=0x3A79A0,
    scripts=[
        subroutine_0x3A7999,
    ],
)

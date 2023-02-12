from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A81F6,
)
from .contents.subroutine_0x3A81F6 import script as subroutine_0x3A81F6

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A81F6,
    start=0x3A81F6,
    end=0x3A821D,
    scripts=[
        subroutine_0x3A81F6,
    ],
)

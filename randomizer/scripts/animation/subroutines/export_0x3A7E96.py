from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A7E96,
)
from .contents.subroutine_0x3A7E96 import script as subroutine_0x3A7E96

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A7E96,
    start=0x3A7E96,
    end=0x3A7EA6,
    scripts=[
        subroutine_0x3A7E96,
    ],
)

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3AC1F1,
)
from .contents.subroutine_0x3AC1F1 import script as subroutine_0x3AC1F1

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3AC1F1,
    start=0x3AC1F1,
    end=0x3AC777,
    scripts=[
        subroutine_0x3AC1F1,
    ],
)

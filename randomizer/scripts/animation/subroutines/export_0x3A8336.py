from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A8336,
)
from .contents.subroutine_0x3A8336 import script as subroutine_0x3A8336

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A8336,
    start=0x3A8336,
    end=0x3A8349,
    scripts=[
        subroutine_0x3A8336,
    ],
)

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3580B4,
)
from .contents.subroutine_0x3580B4 import script as subroutine_0x3580B4

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3580B4,
    start=0x3580B4,
    end=0x358132,
    scripts=[
        subroutine_0x3580B4,
    ],
)

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3531F8,
)
from .contents.subroutine_0x3531F8 import script as subroutine_0x3531F8

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3531F8,
    start=0x3531F8,
    end=0x3532D0,
    scripts=[
        subroutine_0x3531F8,
    ],
)

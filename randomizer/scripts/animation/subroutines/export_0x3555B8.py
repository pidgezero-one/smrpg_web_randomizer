from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3555B8,
)
from .contents.subroutine_0x3555B8 import script as subroutine_0x3555B8

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3555B8,
    start=0x3555B8,
    end=0x3555D4,
    scripts=[
        subroutine_0x3555B8,
    ],
)

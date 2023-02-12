from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X357FA0,
)
from .contents.subroutine_0x357FA0 import script as subroutine_0x357FA0

bank = AnimationScriptBank(
    name=SUBROUTINES_0X357FA0,
    start=0x357FA0,
    end=0x357FE1,
    scripts=[
        subroutine_0x357FA0,
    ],
)

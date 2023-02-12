from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X356089,
)
from .contents.subroutine_0x356089 import script as subroutine_0x356089

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356089,
    start=0x356089,
    end=0x3560A8,
    scripts=[
        subroutine_0x356089,
    ],
)

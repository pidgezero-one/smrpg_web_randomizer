from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X352EBD,
)
from .contents.subroutine_0x352EBD import script as subroutine_0x352EBD

bank = AnimationScriptBank(
    name=SUBROUTINES_0X352EBD,
    start=0x352EBD,
    end=0x352ECE,
    scripts=[
        subroutine_0x352EBD,
    ],
)

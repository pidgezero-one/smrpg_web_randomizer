from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X359C13,
)
from .contents.subroutine_0x359C13 import script as subroutine_0x359C13

bank = AnimationScriptBank(
    name=SUBROUTINES_0X359C13,
    start=0x359C13,
    end=0x359E0A,
    scripts=[
        subroutine_0x359C13,
    ],
)

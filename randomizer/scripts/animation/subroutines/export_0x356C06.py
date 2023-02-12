from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X356C06,
)
from .contents.subroutine_0x356C06 import script as subroutine_0x356C06

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356C06,
    start=0x356C06,
    end=0x356C87,
    scripts=[
        subroutine_0x356C06,
    ],
)

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X356078,
)
from .contents.subroutine_0x356078 import script as subroutine_0x356078

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356078,
    start=0x356078,
    end=0x356086,
    scripts=[
        subroutine_0x356078,
    ],
)

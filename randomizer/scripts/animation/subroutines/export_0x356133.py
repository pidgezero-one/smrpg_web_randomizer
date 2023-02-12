from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X356133,
)
from .contents.subroutine_0x356133 import script as subroutine_0x356133

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356133,
    start=0x356133,
    end=0x356151,
    scripts=[
        subroutine_0x356133,
    ],
)

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X356154,
)
from .contents.subroutine_0x356154 import script as subroutine_0x356154

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356154,
    start=0x356154,
    end=0x356179,
    scripts=[
        subroutine_0x356154,
    ],
)

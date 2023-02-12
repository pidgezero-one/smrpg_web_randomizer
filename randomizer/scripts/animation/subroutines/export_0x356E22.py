from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X356E22,
)
from .contents.subroutine_0x356E22 import script as subroutine_0x356E22

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356E22,
    start=0x356E22,
    end=0x356EAF,
    scripts=[
        subroutine_0x356E22,
    ],
)

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X356061,
)
from .contents.subroutine_0x356061 import script as subroutine_0x356061

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356061,
    start=0x356061,
    end=0x356075,
    scripts=[
        subroutine_0x356061,
    ],
)

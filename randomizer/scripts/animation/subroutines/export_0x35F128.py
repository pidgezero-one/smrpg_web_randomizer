from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35F128,
)
from .contents.subroutine_0x35F128 import script as subroutine_0x35F128

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F128,
    start=0x35F128,
    end=0x35F136,
    scripts=[
        subroutine_0x35F128,
    ],
)

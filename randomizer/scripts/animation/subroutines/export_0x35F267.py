from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35F267,
)
from .contents.subroutine_0x35F267 import script as subroutine_0x35F267

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F267,
    start=0x35F267,
    end=0x35F2B0,
    scripts=[
        subroutine_0x35F267,
    ],
)

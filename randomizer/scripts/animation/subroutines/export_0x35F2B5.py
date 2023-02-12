from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35F2B5,
)
from .contents.subroutine_0x35F2B5 import script as subroutine_0x35F2B5

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F2B5,
    start=0x35F2B5,
    end=0x35F2FE,
    scripts=[
        subroutine_0x35F2B5,
    ],
)

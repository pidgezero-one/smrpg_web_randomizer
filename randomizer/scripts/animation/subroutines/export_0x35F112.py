from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35F112,
)
from .contents.subroutine_0x35F112 import script as subroutine_0x35F112

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F112,
    start=0x35F112,
    end=0x35F123,
    scripts=[
        subroutine_0x35F112,
    ],
)

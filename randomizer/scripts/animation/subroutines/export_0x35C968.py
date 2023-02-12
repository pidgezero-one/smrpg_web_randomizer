from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35C968,
)
from .contents.subroutine_0x35C968 import script as subroutine_0x35C968

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35C968,
    start=0x35C968,
    end=0x35C991,
    scripts=[
        subroutine_0x35C968,
    ],
)

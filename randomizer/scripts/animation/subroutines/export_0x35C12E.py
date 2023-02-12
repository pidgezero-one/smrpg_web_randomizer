from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35C12E,
)
from .contents.subroutine_0x35C12E import script as subroutine_0x35C12E

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35C12E,
    start=0x35C12E,
    end=0x35C292,
    scripts=[
        subroutine_0x35C12E,
    ],
)

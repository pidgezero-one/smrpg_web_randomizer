from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35C307,
)
from .contents.subroutine_0x35C307 import script as subroutine_0x35C307

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35C307,
    start=0x35C307,
    end=0x35C362,
    scripts=[
        subroutine_0x35C307,
    ],
)

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35B365,
)
from .contents.subroutine_0x35B365 import script as subroutine_0x35B365

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35B365,
    start=0x35B365,
    end=0x35B43C,
    scripts=[
        subroutine_0x35B365,
    ],
)

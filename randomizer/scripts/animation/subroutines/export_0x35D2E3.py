from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35D2E3,
)
from .contents.subroutine_0x35D2E3 import script as subroutine_0x35D2E3

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35D2E3,
    start=0x35D2E3,
    end=0x35D38D,
    scripts=[
        subroutine_0x35D2E3,
    ],
)

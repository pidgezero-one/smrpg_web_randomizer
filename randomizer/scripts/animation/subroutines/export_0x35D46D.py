from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35D46D,
)
from .contents.subroutine_0x35D46D import script as subroutine_0x35D46D

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35D46D,
    start=0x35D46D,
    end=0x35D74A,
    scripts=[
        subroutine_0x35D46D,
    ],
)

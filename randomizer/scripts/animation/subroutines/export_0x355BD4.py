from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X355BD4,
)
from .contents.subroutine_0x355BD4 import script as subroutine_0x355BD4

bank = AnimationScriptBank(
    name=SUBROUTINES_0X355BD4,
    start=0x355BD4,
    end=0x355DB5,
    scripts=[
        subroutine_0x355BD4,
    ],
)

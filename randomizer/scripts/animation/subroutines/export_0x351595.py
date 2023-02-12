from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X351595,
)
from .contents.subroutine_0x351595 import script as subroutine_0x351595

bank = AnimationScriptBank(
    name=SUBROUTINES_0X351595,
    start=0x351595,
    end=0x352127,
    scripts=[
        subroutine_0x351595,
    ],
)

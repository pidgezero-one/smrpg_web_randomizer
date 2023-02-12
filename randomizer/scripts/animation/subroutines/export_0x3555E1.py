from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3555E1,
)
from .contents.subroutine_0x3555E1 import script as subroutine_0x3555E1

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3555E1,
    start=0x3555E1,
    end=0x3556E2,
    scripts=[
        subroutine_0x3555E1,
    ],
)

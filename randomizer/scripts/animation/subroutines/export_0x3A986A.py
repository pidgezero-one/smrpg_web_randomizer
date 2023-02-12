from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A986A,
)
from .contents.subroutine_0x3A986A import script as subroutine_0x3A986A

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A986A,
    start=0x3A986A,
    end=0x3A9D74,
    scripts=[
        subroutine_0x3A986A,
    ],
)

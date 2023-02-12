from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A84E4,
)
from .contents.subroutine_0x3A84E4 import script as subroutine_0x3A84E4

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A84E4,
    start=0x3A84E4,
    end=0x3A84ED,
    scripts=[
        subroutine_0x3A84E4,
    ],
)

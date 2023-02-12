from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A7E4B,
)
from .contents.subroutine_0x3A7E4B import script as subroutine_0x3A7E4B

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A7E4B,
    start=0x3A7E4B,
    end=0x3A7E5C,
    scripts=[
        subroutine_0x3A7E4B,
    ],
)

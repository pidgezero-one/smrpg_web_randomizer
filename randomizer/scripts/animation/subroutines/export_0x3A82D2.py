from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A82D2,
)
from .contents.subroutine_0x3A82D2 import script as subroutine_0x3A82D2

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A82D2,
    start=0x3A82D2,
    end=0x3A82E5,
    scripts=[
        subroutine_0x3A82D2,
    ],
)

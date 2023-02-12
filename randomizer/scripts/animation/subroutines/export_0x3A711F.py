from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A711F,
)
from .contents.subroutine_0x3A711F import script as subroutine_0x3A711F

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A711F,
    start=0x3A711F,
    end=0x3A715C,
    scripts=[
        subroutine_0x3A711F,
    ],
)

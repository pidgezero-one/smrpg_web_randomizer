from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X353C82,
)
from .contents.subroutine_0x353C82 import script as subroutine_0x353C82

bank = AnimationScriptBank(
    name=SUBROUTINES_0X353C82,
    start=0x353C82,
    end=0x353DCB,
    scripts=[
        subroutine_0x353C82,
    ],
)

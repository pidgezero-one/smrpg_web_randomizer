from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X350402,
)
from .contents.subroutine_0x350402 import script as subroutine_0x350402

bank = AnimationScriptBank(
    name=SUBROUTINES_0X350402,
    start=0x350402,
    end=0x350467,
    scripts=[
        subroutine_0x350402,
    ],
)

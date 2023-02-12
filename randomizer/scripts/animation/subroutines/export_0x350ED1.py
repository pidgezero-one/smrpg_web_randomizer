from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X350ED1,
)
from .contents.subroutine_0x350ED1 import script as subroutine_0x350ED1

bank = AnimationScriptBank(
    name=SUBROUTINES_0X350ED1,
    start=0x350ED1,
    end=0x350EED,
    scripts=[
        subroutine_0x350ED1,
    ],
)

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X359252,
)
from .contents.subroutine_0x359252 import script as subroutine_0x359252

bank = AnimationScriptBank(
    name=SUBROUTINES_0X359252,
    start=0x359252,
    end=0x359396,
    scripts=[
        subroutine_0x359252,
    ],
)

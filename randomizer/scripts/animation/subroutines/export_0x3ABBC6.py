from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3ABBC6,
)
from .contents.subroutine_0x3ABBC6 import script as subroutine_0x3ABBC6

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3ABBC6,
    start=0x3ABBC6,
    end=0x3AC146,
    scripts=[
        subroutine_0x3ABBC6,
    ],
)

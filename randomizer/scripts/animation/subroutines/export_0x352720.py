from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X352720,
)
from .contents.subroutine_0x352720 import script as subroutine_0x352720

bank = AnimationScriptBank(
    name=SUBROUTINES_0X352720,
    start=0x352720,
    end=0x352731,
    scripts=[
        subroutine_0x352720,
    ],
)

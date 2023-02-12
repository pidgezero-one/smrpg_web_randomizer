from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X352B20,
)
from .contents.subroutine_0x352B20 import script as subroutine_0x352B20

bank = AnimationScriptBank(
    name=SUBROUTINES_0X352B20,
    start=0x352B20,
    end=0x352B28,
    scripts=[
        subroutine_0x352B20,
    ],
)

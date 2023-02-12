from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X352C2F,
)
from .contents.subroutine_0x352C2F import script as subroutine_0x352C2F

bank = AnimationScriptBank(
    name=SUBROUTINES_0X352C2F,
    start=0x352C2F,
    end=0x352C40,
    scripts=[
        subroutine_0x352C2F,
    ],
)

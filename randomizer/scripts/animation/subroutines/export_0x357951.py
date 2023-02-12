from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X357951,
)
from .contents.subroutine_0x357951 import script as subroutine_0x357951

bank = AnimationScriptBank(
    name=SUBROUTINES_0X357951,
    start=0x357951,
    end=0x3579A0,
    scripts=[
        subroutine_0x357951,
    ],
)

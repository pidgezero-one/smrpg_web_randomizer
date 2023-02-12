from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X357C57,
)
from .contents.subroutine_0x357C57 import script as subroutine_0x357C57

bank = AnimationScriptBank(
    name=SUBROUTINES_0X357C57,
    start=0x357C57,
    end=0x357CF5,
    scripts=[
        subroutine_0x357C57,
    ],
)

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X354E72,
)
from .contents.subroutine_0x354E72 import script as subroutine_0x354E72

bank = AnimationScriptBank(
    name=SUBROUTINES_0X354E72,
    start=0x354E72,
    end=0x354F10,
    scripts=[
        subroutine_0x354E72,
    ],
)

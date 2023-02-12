from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3AC7CF,
)
from .contents.subroutine_0x3AC7CF import script as subroutine_0x3AC7CF

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3AC7CF,
    start=0x3AC7CF,
    end=0x3ACCAF,
    scripts=[
        subroutine_0x3AC7CF,
    ],
)

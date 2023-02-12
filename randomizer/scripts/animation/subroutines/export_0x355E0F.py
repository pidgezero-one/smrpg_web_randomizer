from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X355E0F,
)
from .contents.subroutine_0x355E0F import script as subroutine_0x355E0F

bank = AnimationScriptBank(
    name=SUBROUTINES_0X355E0F,
    start=0x355E0F,
    end=0x355F1C,
    scripts=[
        subroutine_0x355E0F,
    ],
)

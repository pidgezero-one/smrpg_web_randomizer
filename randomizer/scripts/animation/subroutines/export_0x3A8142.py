from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A8142,
)
from .contents.subroutine_0x3A8142 import script as subroutine_0x3A8142

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A8142,
    start=0x3A8142,
    end=0x3A8155,
    scripts=[
        subroutine_0x3A8142,
    ],
)

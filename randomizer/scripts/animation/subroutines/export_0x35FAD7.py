from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35FAD7,
)
from .contents.subroutine_0x35FAD7 import script as subroutine_0x35FAD7

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35FAD7,
    start=0x35FAD7,
    end=0x35FC88,
    scripts=[
        subroutine_0x35FAD7,
    ],
)

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A7DE5,
)
from .contents.subroutine_0x3A7DE5 import script as subroutine_0x3A7DE5

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A7DE5,
    start=0x3A7DE5,
    end=0x3A7DEC,
    scripts=[
        subroutine_0x3A7DE5,
    ],
)

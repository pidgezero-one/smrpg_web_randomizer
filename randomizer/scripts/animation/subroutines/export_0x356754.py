from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X356754,
)
from .contents.subroutine_0x356754 import script as subroutine_0x356754

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356754,
    start=0x356754,
    end=0x35678A,
    scripts=[
        subroutine_0x356754,
    ],
)

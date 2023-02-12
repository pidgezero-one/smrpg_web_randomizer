from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X356831,
)
from .contents.subroutine_0x356831 import script as subroutine_0x356831

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356831,
    start=0x356831,
    end=0x356918,
    scripts=[
        subroutine_0x356831,
    ],
)

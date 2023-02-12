from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X358323,
)
from .contents.subroutine_0x358323 import script as subroutine_0x358323

bank = AnimationScriptBank(
    name=SUBROUTINES_0X358323,
    start=0x358323,
    end=0x35837B,
    scripts=[
        subroutine_0x358323,
    ],
)

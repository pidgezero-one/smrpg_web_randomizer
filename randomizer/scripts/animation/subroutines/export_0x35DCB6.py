from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35DCB6,
)
from .contents.subroutine_0x35DCB6 import script as subroutine_0x35DCB6

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35DCB6,
    start=0x35DCB6,
    end=0x35DCD4,
    scripts=[
        subroutine_0x35DCB6,
    ],
)

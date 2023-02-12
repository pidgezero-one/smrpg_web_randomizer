from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35DD01,
)
from .contents.subroutine_0x35DD01 import script as subroutine_0x35DD01

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35DD01,
    start=0x35DD01,
    end=0x35DFC7,
    scripts=[
        subroutine_0x35DD01,
    ],
)

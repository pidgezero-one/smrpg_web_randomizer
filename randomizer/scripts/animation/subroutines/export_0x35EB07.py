from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35EB07,
)
from .contents.subroutine_0x35EB07 import script as subroutine_0x35EB07

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35EB07,
    start=0x35EB07,
    end=0x35ECA1,
    scripts=[
        subroutine_0x35EB07,
    ],
)

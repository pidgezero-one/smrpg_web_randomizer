from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3557CE,
)
from .contents.subroutine_0x3557CE import script as subroutine_0x3557CE

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3557CE,
    start=0x3557CE,
    end=0x3558A7,
    scripts=[
        subroutine_0x3557CE,
    ],
)

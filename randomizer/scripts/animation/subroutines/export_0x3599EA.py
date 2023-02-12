from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3599EA,
)
from .contents.subroutine_0x3599EA import script as subroutine_0x3599EA

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3599EA,
    start=0x3599EA,
    end=0x359C08,
    scripts=[
        subroutine_0x3599EA,
    ],
)

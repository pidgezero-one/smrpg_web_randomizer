from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A9EC1,
)
from .contents.subroutine_0x3A9EC1 import script as subroutine_0x3A9EC1

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A9EC1,
    start=0x3A9EC1,
    end=0x3A9F8A,
    scripts=[
        subroutine_0x3A9EC1,
    ],
)

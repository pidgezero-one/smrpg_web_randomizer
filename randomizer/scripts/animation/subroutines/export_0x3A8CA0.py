from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A8CA0,
)
from .contents.subroutine_0x3A8CA0 import script as subroutine_0x3A8CA0

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A8CA0,
    start=0x3A8CA0,
    end=0x3A8E6F,
    scripts=[
        subroutine_0x3A8CA0,
    ],
)

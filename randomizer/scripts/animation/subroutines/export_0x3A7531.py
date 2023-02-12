from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A7531,
)
from .contents.subroutine_0x3A7531 import script as subroutine_0x3A7531

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A7531,
    start=0x3A7531,
    end=0x3A7551,
    scripts=[
        subroutine_0x3A7531,
    ],
)

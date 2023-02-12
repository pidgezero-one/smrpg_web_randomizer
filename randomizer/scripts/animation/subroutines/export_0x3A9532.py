from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A9532,
)
from .contents.subroutine_0x3A9532 import script as subroutine_0x3A9532

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A9532,
    start=0x3A9532,
    end=0x3A96B8,
    scripts=[
        subroutine_0x3A9532,
    ],
)

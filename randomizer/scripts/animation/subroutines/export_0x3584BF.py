from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3584BF,
)
from .contents.subroutine_0x3584BF import script as subroutine_0x3584BF

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3584BF,
    start=0x3584BF,
    end=0x358684,
    scripts=[
        subroutine_0x3584BF,
    ],
)

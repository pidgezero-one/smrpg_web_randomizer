from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A78B8,
)
from .contents.subroutine_0x3A78B8 import script as subroutine_0x3A78B8

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A78B8,
    start=0x3A78B8,
    end=0x3A78C0,
    scripts=[
        subroutine_0x3A78B8,
    ],
)

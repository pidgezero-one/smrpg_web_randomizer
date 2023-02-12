from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35ABD9,
)
from .contents.subroutine_0x35ABD9 import script as subroutine_0x35ABD9

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35ABD9,
    start=0x35ABD9,
    end=0x35ABF5,
    scripts=[
        subroutine_0x35ABD9,
    ],
)

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35BEB8,
)
from .contents.subroutine_0x35BEB8 import script as subroutine_0x35BEB8

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35BEB8,
    start=0x35BEB8,
    end=0x35BF61,
    scripts=[
        subroutine_0x35BEB8,
    ],
)

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35EA16,
)
from .contents.subroutine_0x35EA16 import script as subroutine_0x35EA16

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35EA16,
    start=0x35EA16,
    end=0x35EAF8,
    scripts=[
        subroutine_0x35EA16,
    ],
)

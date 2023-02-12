from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35C29D,
)
from .contents.subroutine_0x35C29D import script as subroutine_0x35C29D

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35C29D,
    start=0x35C29D,
    end=0x35C2DC,
    scripts=[
        subroutine_0x35C29D,
    ],
)

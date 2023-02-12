from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35F825,
)
from .contents.subroutine_0x35F825 import script as subroutine_0x35F825

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F825,
    start=0x35F825,
    end=0x35F92B,
    scripts=[
        subroutine_0x35F825,
    ],
)

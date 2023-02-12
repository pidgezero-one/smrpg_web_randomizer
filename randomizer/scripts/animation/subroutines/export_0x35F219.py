from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35F219,
)
from .contents.subroutine_0x35F219 import script as subroutine_0x35F219

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F219,
    start=0x35F219,
    end=0x35F262,
    scripts=[
        subroutine_0x35F219,
    ],
)

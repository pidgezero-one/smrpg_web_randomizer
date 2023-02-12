from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35BA9B,
)
from .contents.subroutine_0x35BA9B import script as subroutine_0x35BA9B

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35BA9B,
    start=0x35BA9B,
    end=0x35BBC6,
    scripts=[
        subroutine_0x35BA9B,
    ],
)

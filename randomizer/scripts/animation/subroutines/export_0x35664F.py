from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35664F,
)
from .contents.subroutine_0x35664F import script as subroutine_0x35664F

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35664F,
    start=0x35664F,
    end=0x3566BE,
    scripts=[
        subroutine_0x35664F,
    ],
)

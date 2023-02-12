from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3556ED,
)
from .contents.subroutine_0x3556ED import script as subroutine_0x3556ED

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3556ED,
    start=0x3556ED,
    end=0x3557C5,
    scripts=[
        subroutine_0x3556ED,
    ],
)

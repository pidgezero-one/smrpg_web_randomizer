from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A9725,
)
from .contents.subroutine_0x3A9725 import script as subroutine_0x3A9725

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A9725,
    start=0x3A9725,
    end=0x3A97CD,
    scripts=[
        subroutine_0x3A9725,
    ],
)

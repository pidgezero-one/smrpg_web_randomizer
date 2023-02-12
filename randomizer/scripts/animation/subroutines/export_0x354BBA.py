from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X354BBA,
)
from .contents.subroutine_0x354BBA import script as subroutine_0x354BBA

bank = AnimationScriptBank(
    name=SUBROUTINES_0X354BBA,
    start=0x354BBA,
    end=0x354C83,
    scripts=[
        subroutine_0x354BBA,
    ],
)

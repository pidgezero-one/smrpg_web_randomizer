from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A855C,
)
from .contents.subroutine_0x3A855C import script as subroutine_0x3A855C

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A855C,
    start=0x3A855C,
    end=0x3A8579,
    scripts=[
        subroutine_0x3A855C,
    ],
)

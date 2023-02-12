from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A96BD,
)
from .contents.subroutine_0x3A96BD import script as subroutine_0x3A96BD

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A96BD,
    start=0x3A96BD,
    end=0x3A971C,
    scripts=[
        subroutine_0x3A96BD,
    ],
)

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35B46F,
)
from .contents.subroutine_0x35B46F import script as subroutine_0x35B46F

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35B46F,
    start=0x35B46F,
    end=0x35B5FF,
    scripts=[
        subroutine_0x35B46F,
    ],
)

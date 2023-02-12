from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35061E,
)
from .contents.subroutine_0x35061E import script as subroutine_0x35061E

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35061E,
    start=0x35061E,
    end=0x3506FF,
    scripts=[
        subroutine_0x35061E,
    ],
)

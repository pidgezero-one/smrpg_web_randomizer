from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A9D7B,
)
from .contents.subroutine_0x3A9D7B import script as subroutine_0x3A9D7B

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A9D7B,
    start=0x3A9D7B,
    end=0x3A9EB6,
    scripts=[
        subroutine_0x3A9D7B,
    ],
)

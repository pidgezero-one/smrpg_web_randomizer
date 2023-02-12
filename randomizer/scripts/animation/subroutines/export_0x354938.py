from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X354938,
)
from .contents.subroutine_0x354938 import script as subroutine_0x354938

bank = AnimationScriptBank(
    name=SUBROUTINES_0X354938,
    start=0x354938,
    end=0x354A17,
    scripts=[
        subroutine_0x354938,
    ],
)

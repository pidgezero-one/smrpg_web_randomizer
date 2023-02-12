from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_32_0X350C14,
)
from .contents.subroutine_0x32 import script as subroutine_0x32

bank = AnimationScriptBank(
    name=BEHAVIOUR_32_0X350C14,
    start=0x350C14,
    end=0x350C5A,
    scripts=[
        subroutine_0x32,
    ],
)

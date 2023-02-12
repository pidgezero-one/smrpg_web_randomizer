from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_31_0X350BFD,
)
from .contents.subroutine_0x31 import script as subroutine_0x31

bank = AnimationScriptBank(
    name=BEHAVIOUR_31_0X350BFD,
    start=0x350BFD,
    end=0x350C0D,
    scripts=[
        subroutine_0x31,
    ],
)

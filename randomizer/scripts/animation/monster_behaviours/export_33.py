from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_33_0X350C5B,
)
from .contents.subroutine_0x33 import script as subroutine_0x33

bank = AnimationScriptBank(
    name=BEHAVIOUR_33_0X350C5B,
    start=0x350C5B,
    end=0x350C9D,
    scripts=[
        subroutine_0x33,
    ],
)

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_3_0X350669,
)
from .contents.subroutine_0x3 import script as subroutine_0x3

bank = AnimationScriptBank(
    name=BEHAVIOUR_3_0X350669,
    start=0x350669,
    end=0x3506A6,
    scripts=[
        subroutine_0x3,
    ],
)

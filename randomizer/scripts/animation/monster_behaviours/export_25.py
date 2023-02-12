from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_25_0X350ABD,
)
from .contents.subroutine_0x25 import script as subroutine_0x25

bank = AnimationScriptBank(
    name=BEHAVIOUR_25_0X350ABD,
    start=0x350ABD,
    end=0x350AD2,
    scripts=[
        subroutine_0x25,
    ],
)

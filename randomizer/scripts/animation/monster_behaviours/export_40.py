from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_40_0X350DA3,
)
from .contents.subroutine_0x40 import script as subroutine_0x40

bank = AnimationScriptBank(
    name=BEHAVIOUR_40_0X350DA3,
    start=0x350DA3,
    end=0x350DAE,
    scripts=[
        subroutine_0x40,
    ],
)

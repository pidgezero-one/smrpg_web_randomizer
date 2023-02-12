from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_23_0X350A55,
)
from .contents.subroutine_0x23 import script as subroutine_0x23

bank = AnimationScriptBank(
    name=BEHAVIOUR_23_0X350A55,
    start=0x350A55,
    end=0x350A9B,
    scripts=[
        subroutine_0x23,
    ],
)

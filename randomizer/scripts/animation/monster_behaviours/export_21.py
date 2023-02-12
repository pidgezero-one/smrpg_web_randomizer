from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_21_0X350A38,
)
from .contents.subroutine_0x21 import script as subroutine_0x21

bank = AnimationScriptBank(
    name=BEHAVIOUR_21_0X350A38,
    start=0x350A38,
    end=0x350A3D,
    scripts=[
        subroutine_0x21,
    ],
)

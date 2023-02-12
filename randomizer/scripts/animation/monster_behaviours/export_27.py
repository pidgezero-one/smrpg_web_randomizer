from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_27_0X350B2D,
)
from .contents.subroutine_0x27 import script as subroutine_0x27

bank = AnimationScriptBank(
    name=BEHAVIOUR_27_0X350B2D,
    start=0x350B2D,
    end=0x350B7F,
    scripts=[
        subroutine_0x27,
    ],
)

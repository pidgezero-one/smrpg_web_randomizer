from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_28_0X350BB7,
)
from .contents.subroutine_0x28 import script as subroutine_0x28

bank = AnimationScriptBank(
    name=BEHAVIOUR_28_0X350BB7,
    start=0x350BB7,
    end=0x350BF2,
    scripts=[
        subroutine_0x28,
    ],
)

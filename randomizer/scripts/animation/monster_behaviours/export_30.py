from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_30_0X350BF9,
)
from .contents.subroutine_0x30 import script as subroutine_0x30

bank = AnimationScriptBank(
    name=BEHAVIOUR_30_0X350BF9,
    start=0x350BF9,
    end=0x350BFC,
    scripts=[
        subroutine_0x30,
    ],
)

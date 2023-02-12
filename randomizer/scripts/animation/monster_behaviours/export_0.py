from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_0_0X3505C6,
)
from .contents.subroutine_0x0 import script as subroutine_0x0

bank = AnimationScriptBank(
    name=BEHAVIOUR_0_0X3505C6,
    start=0x3505C6,
    end=0x3505D9,
    scripts=[
        subroutine_0x0,
    ],
)

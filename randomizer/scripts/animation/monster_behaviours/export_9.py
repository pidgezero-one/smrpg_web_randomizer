from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_9_0X3507E9,
)
from .contents.subroutine_0x9 import script as subroutine_0x9

bank = AnimationScriptBank(
    name=BEHAVIOUR_9_0X3507E9,
    start=0x3507E9,
    end=0x35082F,
    scripts=[
        subroutine_0x9,
    ],
)

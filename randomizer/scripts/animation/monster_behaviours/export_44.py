from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_44_0X350E4A,
)
from .contents.subroutine_0x44 import script as subroutine_0x44

bank = AnimationScriptBank(
    name=BEHAVIOUR_44_0X350E4A,
    start=0x350E4A,
    end=0x350E5F,
    scripts=[
        subroutine_0x44,
    ],
)

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_51_0X350F56,
)
from .contents.subroutine_0x51 import script as subroutine_0x51

bank = AnimationScriptBank(
    name=BEHAVIOUR_51_0X350F56,
    start=0x350F56,
    end=0x350F6A,
    scripts=[
        subroutine_0x51,
    ],
)

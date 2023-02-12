from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_12_0X3508A4,
)
from .contents.subroutine_0x12 import script as subroutine_0x12

bank = AnimationScriptBank(
    name=BEHAVIOUR_12_0X3508A4,
    start=0x3508A4,
    end=0x3508B9,
    scripts=[
        subroutine_0x12,
    ],
)

from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_46_0X350E98,
)
from .contents.subroutine_0x46 import script as subroutine_0x46

bank = AnimationScriptBank(
    name=BEHAVIOUR_46_0X350E98,
    start=0x350E98,
    end=0x350ED0,
    scripts=[
        subroutine_0x46,
    ],
)

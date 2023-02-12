from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_43_0X350E38,
)
from .contents.subroutine_0x43 import script as subroutine_0x43

bank = AnimationScriptBank(
    name=BEHAVIOUR_43_0X350E38,
    start=0x350E38,
    end=0x350E49,
    scripts=[
        subroutine_0x43,
    ],
)

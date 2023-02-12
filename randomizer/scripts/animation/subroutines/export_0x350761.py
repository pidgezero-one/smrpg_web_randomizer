from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X350761,
)
from .contents.subroutine_0x350761 import script as subroutine_0x350761

bank = AnimationScriptBank(
    name=SUBROUTINES_0X350761,
    start=0x350761,
    end=0x350761,
    scripts=[
        subroutine_0x350761,
    ],
)

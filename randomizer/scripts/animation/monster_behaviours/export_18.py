from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_18_0X35099D,
)
from .contents.subroutine_0x18 import script as subroutine_0x18

bank = AnimationScriptBank(
    name=BEHAVIOUR_18_0X35099D,
    start=0x35099D,
    end=0x3509D4,
    scripts=[
        subroutine_0x18,
    ],
)
